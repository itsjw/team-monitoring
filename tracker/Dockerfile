FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /tracker
WORKDIR /tracker
ADD requirements/base.txt /tracker/
ADD requirements/local.txt /tracker/
RUN pip3 install -r local.txt
ADD . /tracker/

EXPOSE 8000
