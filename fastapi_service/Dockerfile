FROM python:3.9-buster

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y

WORKDIR /code

COPY . /code/app

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

RUN useradd --create-home fastapi_service
USER fastapi-service

ENV PYTHONFAULTHANDLER=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
