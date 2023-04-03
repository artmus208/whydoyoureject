from app import db
from sqlalchemy.sql import func
from sqlalchemy import or_

# Done:
# [X]: Создать в модель в БД
# [x]: Сделать выгрузку всех пустых записей

# TODO:
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

    def __repr__(self):
        return f'{self.id}, {self.time_created}, {self.time_updated}, {self.crusher_id}, {self.comment}'

    def as_dict(self):
        d = dict(zip(['id', 'time_crated', 'time_updated', 'crusher_id', 'comment'],
                    [self.id, self.time_created, self.time_updated, self.crusher_id, self.comment]))
        return d
        


    @classmethod
    def get_unfilled_comments(cls):
        # [x]: Сортировать полученный список в порядке возрастания даты
        res = db.session.execute(
            db.select(cls).where(or_(cls.comment == None, cls.comment == ''))
            .order_by(cls.time_created)
            ).scalars()
        return res.all()
    

    @classmethod
    def get_filled_comments(cls):
        # [x]: Сортировать полученный список в порядке возрастания даты
        res = db.session.execute(
            db.select(cls).where(or_(cls.comment != None, cls.comment != ''))
            .order_by(cls.time_created)
            ).scalars()
        res = res.all()[::-1]
        return res

    @classmethod
    def get_first_empty(cls):
        res = db.session.execute(
            db.select(cls).where(or_(cls.comment == None,cls.comment == ''))
        ).scalar()
        return res