# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code/backend_assessment_exercice
COPY requirements.txt /code/backend_assessment_exercice
RUN pip install -r requirements.txt
COPY . /code/