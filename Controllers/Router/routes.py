import os
from flask import Flask
from flask import render_template

template_dir = os.path.abspath('../../Views/templates')
app = Flask(__name__, template_folder=template_dir)


class Routes:
    def __init__(self):
        self.hello_world()

    @app.route('/')
    def hello_world(self):
        return render_template('hello.html', name='Felipe')
