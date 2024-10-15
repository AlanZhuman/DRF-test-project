FROM python:3.12.3-slim

# Установим рабочую директорию
WORKDIR /app

COPY . .
