FROM python:3.7.2

LABEL Author="Alejandro Dotor"
LABEL E-mail="alexdotordp@gmail.com"

RUN mkdir /app
COPY Pipfile* /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --system --deploy

ADD . /app

EXPOSE 5000