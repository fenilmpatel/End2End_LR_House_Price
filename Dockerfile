FROM python:3.7.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

CMD ["gunicorn","--bind","0.0.0.0:$PORT","wsgi"]

