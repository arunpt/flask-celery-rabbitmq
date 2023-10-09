FROM python:3.11-buster

WORKDIR /home/app

COPY requirements.txt /home/app/

RUN pip install -r requirements.txt

COPY . /home/app/