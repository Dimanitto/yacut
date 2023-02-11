import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, ValidationError


def check_correct_url(form, field):
    pattern = re.compile("^[A-Za-z0-9]*$")
    if not pattern.match(field.data):
        raise ValidationError('Недопустимые символы для создания ссылки!')


class URLMapForm(FlaskForm):
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=16),
            Optional(),
            check_correct_url
        ]
    )
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=256)
        ]
    )
    submit = SubmitField('Создать')
