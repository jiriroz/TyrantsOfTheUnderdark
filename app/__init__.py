import datetime
from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
#app.permanent_session_lifetime = datetime.timedelta(days=365)

from app import routes