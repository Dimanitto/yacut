from datetime import datetime
from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(128), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return dict(
            short_link=url_for(
                'redirect_view',
                short_id=self.short,
                _external=True
            ),
            url=self.original,
        )

    def from_dict(self, data) -> None:
        self.original = data.get('url')
        self.short = data.get('custom_id')
