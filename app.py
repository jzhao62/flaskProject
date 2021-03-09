from flask import Flask
import boto3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name + '!'


@app.route('/hello/<phone_number>')
def hello(phone_number):
    sns = boto3.client('sns')
    sns.publish(
        PhoneNumber=phone_number,
        Message=(
            "Hello! Someone just wanted you to know that they're "
            "thinking about you and you rock! - Sent from flaskapp"
        )
    )
    return f'Thanks for stopping by, we are sending {phone_number} a nice text now!'


if __name__ == '__main__':
    app.run()
