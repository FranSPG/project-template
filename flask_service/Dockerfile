FROM python:3.9-buster

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y

WORKDIR /code

COPY . /code/app
RUN pip install --no-cache-dir --upgrade -r /code/app/requirements.txt

RUN useradd --create-home flask-service
USER flask-service

ENV PYTHONFAULTHANDLER=1

ENV FLASK_APP='app/main.py'
#ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]