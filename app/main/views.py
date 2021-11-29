from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app, abort

@main_blueprint.route('/')
def index():
    return render_template('main/index.html')

@main_blueprint.route('/admin')
def admin():
    abort(500)
