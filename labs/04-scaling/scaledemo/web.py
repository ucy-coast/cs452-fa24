from flask import Flask
from redis import Redis
from os import environ

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    container_id = environ['HOSTNAME']
    count = redis.incr('hits-{}'.format(container_id))
    return 'Hello World from container {} ! I have been seen {} times.\n'.format(container_id, count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)