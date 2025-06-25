#!bin/bash
 Name:surya
 age:45
 blood group:a+
 FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

CMD ["python", "app.py"]
