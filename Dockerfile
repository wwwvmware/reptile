FROM python:3.6

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  pipenv && mv /etc/apt/sources.list /etc/apt/sources.list.bak

WORKDIR /etc/apt

COPY sources.list .

RUN  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 && apt-get update && apt-get install -y vim

WORKDIR /root/project