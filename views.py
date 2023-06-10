from flask import Blueprint, render_template

# Все руты тут
views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')
    