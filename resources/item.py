
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from db import db
from models import ItemModel
from schemas import ItemSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("item", __name__, description="Operations on items")


@blp.route("/item")
class Item(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        items = ItemModel.query.all()
        return items

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
            return item
        except SQLAlchemyError:
            abort(400, message="Error, problem adding item data.")

    @jwt_required()
    @blp.response(200, ItemSchema)
    def delete(self):
        try:
            ItemModel.query.delete()
            db.session.commit()
        except SQLAlchemyError:
            abort(400, message="Error, problem deleting items.")


@blp.route("/item/<int:item_id>")
class ItemId(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)

    @jwt_required()
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "item deleted."}




