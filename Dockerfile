FROM alpine:3.6
RUN apk add --update python3 py-pip ca-certificates gcc python3-dev musl-dev postgresql-dev
WORKDIR /triviabot
ADD . /triviabot
RUN pip3 install -r requirements.txt
RUN irc3 config.ini
