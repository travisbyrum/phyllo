FROM python:3.6

RUN pip install pipenv

WORKDIR /usr/src/app

COPY . .

RUN make

EXPOSE 5000

CMD bin/entrypoint.sh
