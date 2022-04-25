from flask import Flask
from flask import render_template
from art import text2art
from flask import request
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from decouple import config
app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
csrf = CSRFProtect(app)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # form = request.form
        # art = make_art(form)
        content = request.get_json()
        font = content['font']

        art = text2art(content['userInput'], font=font)

        return {
            'art': art
        }

    return render_template('index.html')
