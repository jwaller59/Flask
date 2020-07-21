from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


from app import routes

bootstrap = Bootstrap(app)