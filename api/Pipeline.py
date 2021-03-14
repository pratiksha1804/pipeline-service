from flask_restful import Resource
import json, jwt
from flask import request, make_response, jsonify
from config import app
import database
from http import HTTPStatus

app.config['SECRET_KEY'] = 'thisisthesecretkey'

class Pipeline(Resource):
    def post(self):
        try:
            print("data...",request)
            # payload = json.loads(request.data.decode())
            action = request.headers['operation']
            print("action.....",action)
            token = request.headers['X_ACCESS_TOKEN']
            print("token.....",token)

            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            data = database.validatePermission(action,decoded_token['role'])

            if data:
                return make_response(jsonify(
                    {
                        "title": "You are authorized person",
                        "status": HTTPStatus.OK,
                    }
                ),
                    HTTPStatus.OK
                )
            return make_response(jsonify(
                {
                    "title": "You are not authorized person",
                    "status": HTTPStatus.OK,
                }
            ),
                HTTPStatus.OK
            )

        except Exception as e:
            return make_response("error...",e)