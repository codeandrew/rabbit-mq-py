#!/bin/sh

docker build -t rmq-producer-flask .
docker images | grep rmq-producer-flask

echo "What's The Next Version"
read NUM

docker tag rmq-producer-flask codeandrew/rmq-producer-flask:v$NUM
docker push codeandrew/rmq-producer-flask:v$NUM
