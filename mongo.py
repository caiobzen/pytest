from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'languages'
app.config['MONGO_URI'] = 'mongodb://admin:admin@ds117821.mlab.com:17821/languages'

mongo = PyMongo(app)

@app.route('/languages', methods=['GET'])
def get_all_frameworks():
    languages = mongo.db.languages

    output = []

    for q in languages.find():
        output.append({'name' : q['name']})

    return jsonify({'result' : output})

@app.route('/language/<name>', methods=['GET'])
def get_one_framework(name):
    languages = mongo.db.languages

    q = languages.find_one({'name' : name})

    if q:
        output = {'name' : q['name']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
