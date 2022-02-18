from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")
app.config['JSON_AS_ASCII'] = False

from member_system.users.route import users
from member_system.member_api.route import api
from member_system.main.route import main
app.register_blueprint(users)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(main)