
from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    #items = db.relationship("ItemModel", back_populates="store")

    tags = db.relationship("TagModel", back_populates="store")

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}












