# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

CMD [ "python", "main.py"]