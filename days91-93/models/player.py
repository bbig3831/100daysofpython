from datetime import datetime

import sqlalchemy
from models.model_base import ModelBase

class Player(ModelBase):
    __tablename__ = 'player'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)