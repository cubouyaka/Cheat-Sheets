from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello {name}! Welcome to my Flask app."


if __name__ == '__main__':
    app.run()
