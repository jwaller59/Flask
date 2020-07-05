from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap = Bootstrap(app)
from app import routes