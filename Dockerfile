FROM python:3.6

RUN pip install pipenv && apt-get update&&apt-get install -y vim
