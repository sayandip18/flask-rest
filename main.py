from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"name": name, "test": test}


api.add_resource(HelloWorld, "/hello/<string:name>/<int:test>")

if __name__ == "main":
    app.run(debug=True)