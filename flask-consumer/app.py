from flask import Flask, request, Response
import pika

app = Flask(__name__)
i = 0

connection = pika.BlockingConnection(
             pika.ConnectionParameters(host='my-rabbit-rabbitmq-ha'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] Waiting for mesages. To exit press CTRL+C')
channel.start_consuming()


@app.route('/api/consumer/get', methods=['GET'])
def index(i):
    i += 1
    return "Successful returns: {}".format(i)


@app.route('/api/consume/message', methods=['GET'])
def incoming():
    return 'test'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
