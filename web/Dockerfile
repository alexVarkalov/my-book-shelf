FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /www
WORKDIR /www
ADD ./requirements.txt /www/requirements.txt
RUN pip install -r requirements.txt
COPY . /www