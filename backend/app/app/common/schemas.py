from marshmallow import Schema, fields


class Vehicle(Schema):
    id = fields.Int()
    title = fields.String()
    weight = fields.Int()
    range = fields.Int()
