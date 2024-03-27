from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://database:27017/')
db = client['user_data']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    user_data = {
        'name': name,
        'email': email
    }

    collection.insert_one(user_data)

    return jsonify({'message': 'Data submitted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
