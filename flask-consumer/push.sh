#!/bin/sh

docker build -t rmq-consumer-flask .
docker images | grep rmq-consumer-flask

echo "What's The Next Version"
read NUM

docker tag rmq-consumer-flask codeandrew/rmq-consumer-flask:v$NUM
docker push codeandrew/rmq-consumer-flask:v$NUM
