FROM python:3.6-alpine as dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt
ADD . /src