from flask import Flask, request, Response
import pika

app = Flask(__name__)
i = 0


@app.route('/api/produce/get', methods=['GET'])
def index(i):
    i += 1
    return "Successful returns: {}".format(i)


@app.route('/api/produce/message', methods=['POST'])
def incoming():
    connection = pika.BlockingConnection(
                 pika.ConnectionParameters('my-rabbit-rabbitmq-ha'))
    channel = connection.channel()
    data = request.get_data()
    print(data)

    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=data)
    return Response('Data sent was: {}'.format(data), status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
