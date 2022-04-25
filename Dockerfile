# syntax=docker/dockerfile:1
FROM alpine

RUN apk add --no-cache python3-dev && apk add py3-pip

RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN mkdir -p ./app/functions ./app/static
COPY ./functions/* ./app/functions
COPY ./static/* ./app/static
COPY ./temp_content/* ./app/temp_content

RUN pip install -r requirements.txt

CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]