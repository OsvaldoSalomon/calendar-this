from flask import Blueprint
from flask import render_template

bp = Blueprint('main', __name__, '/')

@bp.route('/')
def main():
    return render_template('main.html')
