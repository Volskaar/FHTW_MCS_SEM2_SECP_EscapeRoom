from __future__ import annotations

import os
import re
from html import unescape
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path

from flask import Flask, abort, redirect, render_template, request, session, url_for
from db import get_connection
from seed import initialize_webmail_db

app = Flask(__name__)
app.secret_key = os.environ.get("WEBMAIL_SECRET_KEY", "webmail-secret-key")
app.config["SESSION_COOKIE_NAME"] = os.environ.get(
    "WEBMAIL_SESSION_COOKIE_NAME", "fintech_webmail_session"
)
MAIL_SOURCE_DIR = Path(os.environ.get("MAIL_SOURCE_DIR", "/opt/webmail/email")).resolve()

def _safe_relative_path(relative_path: str) -> Path:
    candidate = (MAIL_SOURCE_DIR / relative_path).resolve()
    if candidate == MAIL_SOURCE_DIR or MAIL_SOURCE_DIR not in candidate.parents:
        abort(404)
    if candidate.suffix.lower() != ".eml":
        abort(404)
    if not candidate.is_file():
        abort(404)
    return candidate

def _strip_html(html_content: str) -> str:
    # Convert common block-level tags to line breaks before removing tags.
    with_breaks = re.sub(r"(?i)<br\\s*/?>", "\n", html_content)
    with_breaks = re.sub(r"(?i)</?(p|div|li|ul|ol|tr|table|h[1-6])[^>]*>", "\n", with_breaks)
    with_breaks = re.sub(r"(?i)<blockquote[^>]*>", "\n\n> ", with_breaks)
    with_breaks = re.sub(r"(?i)</blockquote>", "\n", with_breaks)

    no_scripts = re.sub(r"(?is)<(script|style).*?>.*?</\\1>", " ", with_breaks)
    no_tags = re.sub(r"(?s)<[^>]+>", "", no_scripts)
    decoded = unescape(no_tags)
    decoded = decoded.replace("\xa0", " ")

    # Normalize whitespace per line while preserving intentional line breaks.
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in decoded.splitlines()]
    compact_lines = []
    previous_empty = False
    for line in lines:
        if line == ">":
            continue
        is_empty = line == ""
        if is_empty and previous_empty:
            continue
        compact_lines.append(line)
        previous_empty = is_empty

    return "\n".join(compact_lines).strip()

def _extract_text(message) -> str:
    if message.is_multipart():
        plain_part = message.get_body(preferencelist=("plain",))
        if plain_part is not None:
            return plain_part.get_content().strip()

        html_part = message.get_body(preferencelist=("html",))
        if html_part is not None:
            return _strip_html(html_part.get_content())

        for part in message.walk():
            if part.get_content_type() == "text/plain":
                return part.get_content().strip()
    else:
        content = message.get_content()
        if message.get_content_type() == "text/html":
            return _strip_html(content)
        return content.strip()

    return ""

def _format_date(raw_date: str) -> str:
    if not raw_date:
        return "Unbekannt"
    try:
        parsed = parsedate_to_datetime(raw_date)
        if parsed.tzinfo is None:
            return parsed.strftime("%d.%m.%Y %H:%M")
        local_dt = parsed.astimezone()
        return local_dt.strftime("%d.%m.%Y %H:%M")
    except Exception:
        return raw_date

def _parse_eml(file_path: Path) -> dict:
    with file_path.open("rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    body_text = _extract_text(msg)
    preview = body_text.replace("\n", " ").strip()
    if len(preview) > 170:
        preview = preview[:167].rstrip() + "..."

    return {
        "relative_path": file_path.relative_to(MAIL_SOURCE_DIR).as_posix(),
        "filename": file_path.name,
        "subject": msg.get("subject", "(Ohne Betreff)"),
        "from": msg.get("from", "Unbekannt"),
        "to": msg.get("to", "Unbekannt"),
        "date_raw": msg.get("date", ""),
        "date": _format_date(msg.get("date", "")),
        "body": body_text,
        "preview": preview,
    }

def _collect_mails() -> list[dict]:
    if not MAIL_SOURCE_DIR.exists():
        return []

    mails = []

    for file_path in sorted(MAIL_SOURCE_DIR.rglob("*.eml"), key=lambda p: p.name.lower()):
        try:
            mail = _parse_eml(file_path)
        except Exception:
            continue

        mails.append(mail)

    mails.sort(key=lambda item: item["date_raw"] or "", reverse=True)
    return mails


@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("user"):
        return redirect("/inbox")

    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with get_connection() as conn:
            user = conn.execute(
                """
                SELECT username, role
                FROM webmail_users
                WHERE username = ? AND password = ?
                """,
                (username, password),
            ).fetchone()

        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect("/inbox")

        error = "Login failed"

    return render_template("login.html", error=error)

@app.route("/inbox")
def inbox():
    if "user" not in session:
        return redirect("/")

    mails = _collect_mails()

    selected_mail = mails[0] if mails else None
    selected_path = request.args.get("selected", "")
    if selected_path:
        for mail in mails:
            if mail["relative_path"] == selected_path:
                selected_mail = mail
                break

    return render_template(
        "inbox.html",
        mails=mails,
        selected_mail=selected_mail,
        selected_path=selected_mail["relative_path"] if selected_mail else "",
    )

@app.route("/mail/<path:relative_path>")
def mail_detail(relative_path: str):
    if "user" not in session:
        return redirect("/")

    file_path = _safe_relative_path(relative_path)
    selected_mail = _parse_eml(file_path)

    mails = _collect_mails()

    return render_template(
        "inbox.html",
        mails=mails,
        selected_mail=selected_mail,
        selected_path=selected_mail["relative_path"],
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.context_processor
def utility_processor():
    def mail_link(relative_path: str) -> str:
        return url_for("mail_detail", relative_path=relative_path)

    return {"mail_link": mail_link}


initialize_webmail_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)