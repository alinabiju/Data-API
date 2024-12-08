from flask import Flask, jsonify
from databaseConnector import DatabaseConnector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def homepage():
    return '<h1>Welcome to Api Home</h1>'


# @app.get('/objects/<item_id>', methods=['GET','PUT'])
# def objects_route(item_id):
#     if request.method=='GET':
#         return retrievedata()
#     elif request.method=='PUT':
#         updateObjectState(item_id,request.args.get('new_state'))

@app.get('/objects')
@cross_origin()
def retrievedata():
    db_connector = DatabaseConnector()
    data = db_connector.getAllObjects()

    db_connector.closeConnection()
    return data

@app.put('/objects/<item_id>')
def updateObjectState(item_id):
    db_connector = DatabaseConnector()
    db_connector.updateObjectState(item_id, request.args.get('new_state'))

    db_connector.closeConnection()

if __name__ == '__main__':
    app.run(port=5000,debug= True)