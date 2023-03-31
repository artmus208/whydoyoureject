from app import db
from sqlalchemy.sql import func
from sqlalchemy import or_

# Done:
# [X]: Создать в модель в БД
# [x]: Сделать выгрузку всех пустых записей
class MyBaseClass:
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


class ArchivesCrusherComment(MyBaseClass, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    crusher_id = db.Column(db.Integer)
    comment = db.Column(db.String(255))
    def __init__(self, msg=None):
        self.comment = msg

    @classmethod
    def get_unfilled_comments(cls):
        res = db.session.execute(
            db.select(cls).where(or_(cls.comment == None,cls.comment == ''))
            ).scalars()
        return res
    
    @classmethod
    def get_first_empty(cls):
        res = db.session.execute(
            db.select(cls).where(or_(cls.comment == None,cls.comment == ''))
        ).scalar()
        return res