from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'languages'
app.config['MONGO_URI'] = 'mongodb://admin:admin@ds117821.mlab.com:17821/languages'

mongo = PyMongo(app)

@app.route('/languages', methods=['GET'])
def get_all_frameworks():
    languages = mongo.db.languages

    output = []

    for q in languages.find():
        output.append({'_id' : str(q['_id']), 'name' : q['name'], "creator" : q["creator"], "pictureURL" : q["pictureURL"]})

    return jsonify({'result' : output})

@app.route('/language/<langId>', methods=['GET'])
def get_one_language(langId):
    languages = mongo.db.languages

    q = languages.find_one({'_id' : ObjectId(str(langId))})

    if q:
        output = {'_id' : str(q['_id']),'name' : q['name'], "creator" : q["creator"], "pictureURL" : q["pictureURL"]}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
