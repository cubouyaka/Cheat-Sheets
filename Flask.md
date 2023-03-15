
# Installation
```bash
pip install flask
pip install flask-restful
```

# Basics
## Imports
```python 
from flask import Flask
from flask_restful import Resource, Api
```

## Creating an ordinary Flask called `VideoAPI` 
```python
app = Flask("VideoAPI")
api = Api(app)
```
## Create a class for individual Video that extends `Resource`  and defines the methods for the basics CRUD methods
```python
class Video(Resource):

	def get(self):
		return "GET"
```

## Add this class (Resource) to the Api

In order to have this Resource accessible in the app we need to add this ressource to the api with a url mapping :
```python
api.add_resource(Video, '/')
```

Then we can run the application 
```python
if __name__ == '__main__':
	app.run()
```
