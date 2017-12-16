FROM alpine:3.6
RUN apk add --update python3 py-pip ca-certificates gcc python-dev musl-dev
WORKDIR /triviabot
ADD . /triviabot
RUN pip3 install -r requirements.txt
CMD ["python3", "triviabot/bot.py"]
