
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
```python
@app.route('/greeting/<name>')
def greet_user(name):
    return f'Hello, {name}!'
```
To try it, visit the URL `http://localhost:5000/greeting/Victor` 

7. Create a Flask application that serves a simple HTML page with a form. The form should include a text input field for a name and a submit button. When the form is submitted, the application should display a personalized greeting message that includes the name entered in the form.
```python
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello {name}! Welcome to my Flask app."
```

The `index.html` should be in a directory called `templates` and should look like:
```html
<!DOCTYPE html>
<html>
<head>
	<title>Greeting App</title>
</head>
<body>
	<form action="/greet" method="POST">
		<label for="name">Enter your name:</label>
		<input type="text" name="name" id="name">
		<button type="submit">Submit</button>
	</form>
</body>
</html>
```

8. Write a Flask route that takes in a list of numbers as a URL parameter and returns the sum of those numbers.
```python
@app.route('/sum/<nums>')
def sum(nums):
    num_list = nums.split(',')
    num_sum = 0
    for num in num_list:
        num_sum += int(num)
    return f"The sum of {nums} is {num_sum}."
```

9. Create a Flask application that serves a page with a button. When the button is clicked, the application should make an AJAX call to a separate Flask route that returns a JSON object with a random quote and author.
```python
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_quote')
def random_quote():
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()['content']
    author = response.json()['author']
    return jsonify({'quote': quote, 'author': author})
```

The `index.html` file should look something like this:
```html
<!DOCTYPE html>
<html>
<head>
	<title>Random Quote App</title>
</head>
<body>
	<button onclick="getQuote()">Get a random quote</button>

	<script>
		function getQuote() {
			fetch('/random_quote')
				.then(response => response.json())
				.then(data => {
					alert(`${data.quote}\n- ${data.author}`);
				});
		}
	</script>
</body>
</html>
```

10.  Write a Flask route that takes in a username and password as form data and returns a JSON object with a success message if the credentials are correct, and an error message otherwise.
```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'myusername' and password == 'mypassword':
        return jsonify({'success': True, 'message': 'Login successful.'})
    else:
        return jsonify({'success': False,
```