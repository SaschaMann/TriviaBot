# TriviaBot
A League of Legends Trivia IRC Bot 

## Start everything
`docker-compose build && docker-compose up`

## Start Question Server
`docker run --name triviaquestions --link triviapostgres:postgres --link triviar
edis:redis -p 8080:8080 -d triviaquestions`

## Start TriviaBot
`docker run --name triviabot --link triviapostgres:postgres --link triviaredis:redis --link triviaquestions:triviaquestions -d triviabot`
