

from flask.views import  MethodView
from schemas import StoreSchema
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import StoreModel

blp = Blueprint("store", __name__, description="Operations on store.")


@blp.route("/store")
class Store(MethodView):

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        store = StoreModel.query.all()
        return store

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema())
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
            return store
        except SQLAlchemyError:
            abort(400, message="Error adding store, make sure store name is unique.")

    @blp.response(200, StoreSchema)
    def delete(self):
        try:
            StoreModel.query.delete()
            db.session.commit()
        except SQLAlchemyError:
            abort(400, message="Problem deleting stores.")

@blp.route("/store/<int:store_id>")
class StoreId(MethodView):

    @blp.response(200, StoreSchema)
    def get(self, store_id):
        return StoreModel.query.get_or_404(store_id)

    @blp.response(200, StoreSchema)
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        try:
            db.session.delete(store)
            db.session.commit()
            return store
        except SQLAlchemyError:
            abort(400, message="Problem deleting store")







