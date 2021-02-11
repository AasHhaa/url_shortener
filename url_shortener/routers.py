from flask import Blueprint, render_template, request, redirect
from .models import Link
from .extensions import db
from datetime import datetime, timedelta

short = Blueprint('short', __name__)


@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    if link.short_url_lifetime < datetime.now():
        db.session.delete(link)
        db.session.commit()
        return "Your link is expired", 404
    return redirect(link.original_url)


@short.route('/')
def index():
    return render_template('index.html')


@short.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    lifetime = int(request.form['lifetime']) if request.form['lifetime'] else None
    if lifetime:
        if 1 <= lifetime <= 365:
            lifetime = datetime.now() + timedelta(lifetime)
        else:
            return "Lifetime is not in allowed range",
    else:
        lifetime = datetime.now() + timedelta(90)
    link = Link(original_url=original_url, short_url_lifetime=lifetime)
    db.session.add(link)
    db.session.commit()
    return render_template('link_added.html',
                           new_link=link.short_url,
                           original_url=link.original_url)


@short.errorhandler(404)
def page_not_found(e):
    return '', 404
