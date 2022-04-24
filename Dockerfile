# syntax=docker/dockerfile:1
FROM python:3.6.8-alpine3.9
COPY . .
WORKDIR .

RUN pip install requirements.txt

CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]