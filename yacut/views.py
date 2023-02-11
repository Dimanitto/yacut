import os
import random
import string
from flask import render_template, send_from_directory, flash, redirect, abort
from yacut import app, db, forms, models
from pathlib import Path


if os.getenv('FLASK_ENV') == 'development':
    @app.route('/swagger')
    def swagger_ui():
        return render_template('swagger_ui.html')

    @app.route('/spec')
    def get_spec():
        BASE_DIR = Path(__file__).parent.parent
        return send_from_directory(BASE_DIR, 'openapi.yml')


def get_unique_short_id() -> str:
    """Создания уникального короткого идентификатора"""
    letters = string.ascii_letters
    digits = string.digits
    symbols = letters + digits
    random_url = ''.join(random.choices(symbols, k=6))
    return random_url


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = forms.URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        if models.URLMap.query.filter_by(short=custom_id).first() is not None:
            flash(f'Имя {custom_id} уже занято!', 'unique-error')
            return render_template('url_map.html', form=form)
        url_map = models.URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template('url_map.html', form=form, new_url=custom_id)
    return render_template('url_map.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    url = models.URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)
