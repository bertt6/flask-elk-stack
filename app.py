from flask import Flask
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['http://localhost:9200'])  # Elasticsearch adresi ve portu


@app.route('/hello/<name>')
def hello(name):
    if len(name) < 2:
        es.index(index='flask_logs', body={'name': name, 'message': 'Your name is too short!', 'type': 'error', 'level': 'error'})
        return 'Your name is too short!'
    else:
        es.index(index='flask_logs', body={'name': name, 'message': 'Hello, ' + name + '!', 'type': 'info', 'level': 'info'})
        return f'Hello, {name}!'

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2000)
