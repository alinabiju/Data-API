from flask import Flask

app = Flask(__name__)
@app.route('/mydataportal')
def retrievedata():
    return '<h1>API is working!!!</h1>'

if __name__ == '__main__':
    app.run(port=5000,debug= True)