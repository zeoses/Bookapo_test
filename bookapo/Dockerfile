FROM python:3.10

RUN apt install libpq-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set Environment Variable
ENV TZ="Asia/Tehran"
RUN pip install gunicorn

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN apt-get update && \
    apt-get install -y gettext libgettextpo-dev

COPY . /app
WORKDIR /app

RUN mkdir /var/log/atrcsolaris/staticfiles/*

EXPOSE 8000
