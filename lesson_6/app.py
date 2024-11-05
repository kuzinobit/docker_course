from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('db', 27017)  # Подключение к сервису db по имени
db = client['mydatabase']
collection = db['visits']

@app.route('/') def hello():
    collection.insert_one({'message': 'Hello from Docker Compose!'})
    count = collection.count_documents({})
    return f'Hello from Docker Compose! This page has been visited {count} times.'
if __name__ == '__main__':
    app.run(host='0.0.0.0')