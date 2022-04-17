from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests
from DB import botDB

app = Flask(__name__)
api = Api()


req = {}

parser = reqparse.RequestParser()
parser.add_argument("user_id", type=int)
parser.add_argument("message", type=str)

class Main(Resource):
    def get(self):
        return req[1]

    def delete(self):
        del req[1]
        return req

    def post(self):
        req[len(req) + 1] = parser.parse_args()
        return req

    def put(self):
        req[1] = parser.parse_args()
        return req


api.add_resource(Main, "/api/v1/message/")
api.add_resource(Main, "/api/v1/message_confirmation/")
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="localhost")

    while True:
        status = requests.get("http://localhost:3000/api/v1/message_confirmation/")
        if status.json()["success"]:
            botDB.change_status(status.json()["message_id"], "Корректно")
        else:
            botDB.change_status(status.json()["message_id"], "Заблокировано")