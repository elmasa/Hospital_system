FROM  node:latest
FROM  mysql:latest
FROM  python:latest

WORKDIR /application


RUN  pip install pytest

COPY . .

CMD ["run"]