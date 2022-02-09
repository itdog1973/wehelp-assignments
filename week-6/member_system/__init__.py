from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")


from member_system import routes