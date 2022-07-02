from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


names = {"Wilhelm": {"age": 21, "gender": "male"},
         "Kenta": {"age": 42, "gender": "male"}}
class HelloWorld(Resource):
    def get(self,name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)