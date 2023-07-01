
from db import db


class ItemModel(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=True)

    #store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    #store = db.relationship("StoreModel", back_populates="items")

    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")

