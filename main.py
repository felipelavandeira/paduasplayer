import os
from flask import Flask
from flask import render_template

template_dir = os.path.abspath('./Views/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def hello_world():
    return render_template('hello.html', name='Felipe')


if __name__ == 'main':
    app.run()
