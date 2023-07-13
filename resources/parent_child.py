from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify
from flask_jwt_extended import jwt_required

from db import db
from cache import cache
from models import ParentModel, ChildModel
from schemas import ParentSchema, ChildSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("parent_child", __name__, description="Operations on parent_child")


@blp.route("/parent")
class Parent(MethodView):
    @blp.arguments(ParentSchema)
    def post(self, parent_data):
        parent = ParentModel(**parent_data)
        try:
            db.session.add(parent)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return {"message": "Success"}, 201

    @blp.response(200, ParentSchema(many=True))
    @cache.cached(timeout=10)
    def get(self):
        parents = ParentModel.query.all()
        #return parents
        serialized_parents = ParentSchema().dump(parents)
        return jsonify(serialized_parents)


@blp.route("/parent/<int:parent_id>")
class ParentDelete(MethodView):
    def delete(self, parent_id):
        parent = ParentModel.query.get_or_404(parent_id)
        try:
            db.session.delete(parent)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return {"message": "success"}


@blp.route("/child/<int:parent_id>")
class Child(MethodView):
    @blp.arguments(ChildSchema)
    def post(self, child_data, parent_id):
        child = ChildModel(**child_data, parent_id=parent_id)
        try:
            db.session.add(child)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return {"message": "Success"}, 201


@blp.route("/child")
class ChildGet(MethodView):
    @blp.response(200, ChildSchema(many=True))
    def get(self):
        children = ChildModel.query.all()
        return children


@blp.route("/child/<int:child_id>")
class ChildDelete(MethodView):
    def delete(self, child_id):
        child = ChildModel.query.get_or_404(child_id)
        try:
            db.session.delete(child)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return {"message": "success."}


import logging

logging.basicConfig(level=logging.INFO)
logging.info("hehe")

from flask import request
@blp.route("/test", methods=["GET"])
class TestRoute(MethodView):
    def get(self):
        if request.method == "GET":
            return request.json

