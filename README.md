# TriviaBot
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d53b6c1c72e641478ff9e6f1a9e48763)](https://www.codacy.com/app/SaschaMann/TriviaBot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SaschaMann/TriviaBot&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/d53b6c1c72e641478ff9e6f1a9e48763)](https://www.codacy.com/app/SaschaMann/TriviaBot?utm_source=github.com&utm_medium=referral&utm_content=SaschaMann/TriviaBot&utm_campaign=Badge_Coverage)

A League of Legends Trivia IRC Bot 

## Start everything
`docker-compose build && docker-compose up`

## Start Question Server
`docker run --name triviaquestions --link triviapostgres:postgres --link triviar
edis:redis -p 8080:8080 -d triviaquestions`

## Start TriviaBot
`docker run --name triviabot --link triviapostgres:postgres --link triviaredis:redis --link triviaquestions:triviaquestions -d triviabot`
