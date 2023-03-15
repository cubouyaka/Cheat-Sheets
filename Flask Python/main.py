from flask import Flask
from flask_restful import Resource, Api


class Video(Resource):

    def get(self):
        return "GET"


app = Flask("VideoAPI")
api = Api(app)
api.add_resource(Video, '/')

if __name__ == '__main__':
    app.run()

# Write a Flask route that takes in a user's name as a URL parameter and returns a greeting that includes their name.
