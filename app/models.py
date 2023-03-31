from app import db
from sqlalchemy.sql import func

class MyBaseClass:
    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def commit(self):
        db.session.commit()

    @classmethod
    def get(cls, id):
        try:
            return db.session.get(cls, id)
        except Exception:
            db.session.rollback()
            raise


class ArchivesCrusherComment(db.Model, MyBaseClass):
    crusher_id = db.Column(db.Integer)
    comment = db.Column(db.String(255))
    def __init__(self, msg=None):
        self.comment = msg