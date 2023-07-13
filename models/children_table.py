from db import db

class ChildModel(db.Model):
    __tablename__ = "children_table"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    parent_id = db.Column(db.Integer, db.ForeignKey("parent_table.id"), nullable=False)
    parent = db.relationship("ParentModel", back_populates="children")

