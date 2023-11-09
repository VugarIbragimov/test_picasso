# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# # При старте контейнера запустить сервер разработки.
# CMD ["python", "manage.py", "runserver", "0:8000"]

# Dockerfile

FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/