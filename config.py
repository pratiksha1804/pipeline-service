import os
from flask import Flask
from flask_pymongo import PyMongo
import constants
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
CORS(app)

api=Api(app)
app.config['MONGO_DBNAME'] = "IAM_AUTHENTICATION"
# app.config['MONGO_URI'] = "mongodb://"+constants.MONGO_USERNAME+":"+constants.MONGO_PASSWORD+"@"+constants.MONGO_URL+":"+constants.MONGO_PORT+"?authSource=admin"
app.config['MONGO_URI'] ="mongodb://localhost:27017/IAM_AUTHENTICATION"
mongo = PyMongo(app)