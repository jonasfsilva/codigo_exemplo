FROM python:3.6.8-slim-jessie
LABEL maintainer="Jonas Ferreira"

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code

WORKDIR /code/

CMD [ "python", "rispartest.py" "contas.csv" "transacoes.csv" ]