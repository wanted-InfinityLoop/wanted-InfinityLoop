from flask import Flask
from flask_restful import Resource, Api
from company.models import db

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI']        = "mysql+pymysql://root:1234@localhost:3306/wantedlab"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']  = True

db.init_app(app)
db.app = app
db.create_all()

@app.route("/ping", methods = ['GET'])
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)