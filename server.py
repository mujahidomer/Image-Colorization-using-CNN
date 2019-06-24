from flask import Flask, render_template, request

app = Flask(__name__)

import os

from colorize import eval_one


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_name = file.filename
        ROOT_PATH = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
        model_path = ROOT_PATH + '/models/generation_2/'
        image_path = ROOT_PATH + '/images/testing/' + file.filename
        print image_path
        eval_one.eval(model_path, image_path)
        return render_template('output.html', image=file_name)
    return render_template('index.html')


# server running on port 3000
app.run(port=5000, debug=True)
