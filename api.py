from flask import Flask, jsonify
from databaseConnector import DatabaseConnector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def homepage():
    return '<h1>Welcome to Api Home</h1>'


@app.get('/objects')
def retrievedata():
    db_connector = DatabaseConnector()
    data = db_connector.getAllObjects()

    return data

if __name__ == '__main__':
    app.run(port=5000,debug= True)