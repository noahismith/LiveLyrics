import os
from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from app import db

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/")
def index():
	return render_template('index.html')
