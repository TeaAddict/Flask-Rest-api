from dataclasses import fields

from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=False)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    #store_id = fields.Int(required=True, load_only=True)
    #store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class TagFromStoreSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    #store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    #items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(TagFromStoreSchema()), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PlainChildSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainParentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ParentSchema(PlainParentSchema):
    children = fields.List(fields.Nested(PlainChildSchema()), dump_only=True)


class ChildSchema(PlainChildSchema):
    parent = fields.Nested(PlainParentSchema(), dump_only=True)




