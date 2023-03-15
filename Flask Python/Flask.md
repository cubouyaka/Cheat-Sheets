
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

Then we can make a GET query to the app
```bash 
curl http://localhost:5000/
```


# Example

1.  Before you begin, make sure Flask is installed on your system. You can install Flask by running the command `pip install Flask` in your terminal.
    
2.  Create a new Flask application, let's call it `app.py`, and add the following code to it:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
```

3.  Run the Flask application
```python
python app.py
``` 
Flask will start a local web server on port 5000 by default.

4.  Test the Flask application: Open your web browser and visit the URL `http://localhost:5000/`. You should see the message "Hello, World!" displayed in your browser.

5.  Add a new route to the Flask application. Below the `home()` function:
```python
@app.route('/about')
def about():
    return 'This is the about page!'
```
To see this page, visit the URL `http://localhost:5000/about`.

6.  Write a Flask route that takes in a user's name as a URL parameter and returns a greeting that includes their name.

7. Create a Flask application that serves a simple HTML page with a form. The form should include a text input field for a name and a submit button. When the form is submitted, the application should display a personalized greeting message that includes the name entered in the form.
    
8. Write a Flask route that takes in a list of numbers as a URL parameter and returns the sum of those numbers.

9. Create a Flask application that serves a page with a button. When the button is clicked, the application should make an AJAX call to a separate Flask route that returns a JSON object with a random quote and author.
    
10.  Write a Flask route that takes in a username and password as form data and returns a JSON object with a success message if the credentials are correct, and an error message otherwise.
    
11.  Create a Flask application that serves a page with a button. When the button is clicked, the application should stream a live video feed from the user's webcam.
    
12.  Write a Flask route that serves a JSON object with information about the current weather in a specified location.
    
13.  Create a Flask application that serves a page with a list of items. The user should be able to add new items to the list using a form, and the application should use a database to store the items.
    
14.  Write a Flask route that takes in a CSV file and returns a JSON object with the file's contents.
    
15.  Create a Flask application that serves a page with a form that allows the user to upload a file. The application should store the file in a folder on the server and display a message indicating whether the upload was successful.