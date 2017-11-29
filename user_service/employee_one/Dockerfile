FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /employee_one
WORKDIR /employee_one
ADD requirements/base.txt /employee_one/
ADD requirements/local.txt /employee_one/
RUN pip3 install -r local.txt
ADD . /employee_one/

EXPOSE 8001
