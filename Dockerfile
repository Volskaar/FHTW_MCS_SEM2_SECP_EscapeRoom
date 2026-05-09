FROM python:3.13-slim

WORKDIR /opt/fintech

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY data ./data
COPY backups ./backups

EXPOSE 5000

CMD ["python", "app/app.py"]