from db import db

class ParentModel(db.Model):
    __tablename__ = "parent_table"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    children = db.relationship("ChildModel", cascade="all, delete", back_populates="parent")
    