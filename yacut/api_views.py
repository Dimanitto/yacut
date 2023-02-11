import re
from flask import jsonify, request
from yacut import app, db
from http import HTTPStatus
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .views import get_unique_short_id


def check_custom_id(field: str) -> bool:
    pattern = re.compile("^[A-Za-z0-9]*$")
    return bool(pattern.match(field))


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url_map(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_url_map():
    if not request.data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    custom_id = data.get('custom_id')
    if not custom_id:
        custom_id = get_unique_short_id()
        data['custom_id'] = custom_id
    if not check_custom_id(custom_id) or len(custom_id) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
