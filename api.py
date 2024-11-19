from flask import Flask
from databaseConnector import DatabaseConnector


app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Welcome to Api Home</h1>'


if __name__ == '__main__':
    app.run(port=5000,debug= True)