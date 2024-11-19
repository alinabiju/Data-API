from flask import Flask
from databaseConnector import DatabaseConnector


app = Flask(__name__)

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