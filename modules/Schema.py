from __future__ import annotations

from marshmallow_jsonapi import Schema, fields


class ApiResponseGenerator:
    def generate(self, schema: Schema, status_code: int, message: str):
        schema = schema.dump(schema)
        schema['message'] = message

        return schema, status_code


class ScrapedPriceSchema(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Str()
    whole_price = fields.Str()

    class Meta:
        type_ = "price"

    def create(self) -> ScrapedPriceSchema:
        return self
