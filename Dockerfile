FROM python:3.7

ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /app

RUN apt-get update && apt-get install -y postgresql-client

RUN pipenv install elasticsearch

CMD ["flask", "run"]