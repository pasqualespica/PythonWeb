from datetime import datetime
from config import db, ma
from marshmallow import fields

# SQLAlchemy
class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # https://docs.sqlalchemy.org/en/latest/orm/cascades.html#delete
    notes = db.relationship(
        'Note',
        backref='person',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Note.timestamp)'
    )


    def __str__(self):
        return f" Persona id({self.person_id}) {self.lname}:{self.fname}"


class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


# Marshmallow
# class PersonSchema(ma.Schema):
#     class Meta:
#         model = Person
#         fields = ["person_id", "lname", "fname", "timestamp"]
#         sqla_session = db.session


class PersonSchema(ma.Schema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Person
        sqla_session = db.session

    notes = fields.Nested("PersonNoteSchema", default=[], many=True)


class PersonNoteSchema(ma.Schema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    note_id = fields.Int()
    person_id = fields.Int()
    content = fields.Str()
    timestamp = fields.Str()


class NoteSchema(ma.Schema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Note
        sqla_session = db.session

    person = fields.Nested("NotePersonSchema", default=None)


class NotePersonSchema(ma.Schema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    person_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    timestamp = fields.Str()
