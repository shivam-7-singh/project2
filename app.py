# All the imports go here
from flask import Flask, render_template, redirect, request
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    # Render the HTML file
    return render_template('index.html')


@app.route('/launch_app', methods=['POST'])
def launch_app():
    # Launch the main.py file using subprocess
    subprocess.Popen(['python', 'main.py'])

    # Redirect to the index page or any other page
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
