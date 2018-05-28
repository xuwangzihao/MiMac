from my_app.foundation import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship("TeamUserRelationship", backref="team", lazy='dynamic')
