FROM python:3.13-slim

WORKDIR /opt/webmail

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./app

EXPOSE 5001

CMD ["python", "app/app.py"]