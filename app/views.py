from flask import Blueprint, render_template

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/")
def index():
    return render_template('index.html')


@views_blueprint.route("/lyrics")
def lyrics():
    return render_template('lyrics.html')


@views_blueprint.route("/users")
def users():
    return render_template("users.html")


@views_blueprint.route("/songs")
def songs():
    return render_template("songs.html")


@views_blueprint.route("/contact")
def contact():
    return render_template("contact.html")