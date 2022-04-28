from flask import Flask
from flask import render_template
from art import text2art
from flask import request
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from decouple import config
from flask_assets import Environment, Bundle

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
app.config['WTF_CSRF_TIME_LIMIT'] = 604800
csrf = CSRFProtect(app)
CORS(app)
assets = Environment(app)

scss = Bundle('scss/main.scss', filters='pyscss', output='css/style.css')
assets.register('scss_all', scss)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        content = request.get_json()
        font = content['font']
        user_input = content['userInput']

        art = text2art(user_input, font=font)

        return {
            'art': art
        }

    return render_template('index.html')

  