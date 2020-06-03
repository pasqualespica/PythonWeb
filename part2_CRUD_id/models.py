from datetime import datetime
from config import db, ma

# SQLAlchemy
class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return f" Persona id({self.person_id}) {self.lname}:{self.fname}"

# Marshmallow
class PersonSchema(ma.Schema):
    class Meta:
        model = Person
        fields = ["person_id", "lname", "fname", "timestamp"]
        sqla_session = db.session
