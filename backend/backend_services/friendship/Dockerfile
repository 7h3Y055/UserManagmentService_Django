FROM debian:latest

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3.11-venv python3-pip libpq-dev

COPY ./app .
COPY ./tools/setup.sh .

RUN chmod +x setup.sh

ENTRYPOINT [ "./setup.sh" ]
