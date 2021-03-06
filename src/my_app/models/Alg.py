# -*- coding: utf-8 -*-

from my_app.foundation import db
from my_app.common.constant import BaseAlgorithm


class Alg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base = db.Column(db.SmallInteger, default=BaseAlgorithm.Base)  # 基类
    title = db.Column(db.String(128), unique=True)
    config = db.Column(db.String(4096))
    delete = db.Column(db.Boolean, nullable=False, default=False)
    users = db.relationship("AlgUserRelationship", backref="alg", lazy='dynamic')
    images = db.relationship("Image", backref="alg", lazy='dynamic')

