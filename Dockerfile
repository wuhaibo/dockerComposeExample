# syntax=docker/dockerfile:1
FROM python:3.7

WORKDIR /app
COPY . /app

CMD ["/usr/local/bin/python","/app/main.py"]