import os
from config import app,api
from api.Pipeline import Pipeline

api.add_resource(Pipeline,'/api/pipeline')


if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5003, debug=True)