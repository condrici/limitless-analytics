import unittest

from marshmallow_jsonapi import Schema

from modules.Schema import ScrapedPriceSchema


class TestSchema(unittest.TestCase):

    def test_create(self) -> None:
        price_schema = ScrapedPriceSchema().create()
        price_schema.price = '100,10'
        price_schema.whole_price = '100'

        self.assertIsInstance(price_schema, ScrapedPriceSchema)
        self.assertIsInstance(price_schema, Schema)

        self.assertEqual(price_schema.price, '100,10')
        self.assertEqual(price_schema.whole_price, '100')

        total_class_attributes = len(price_schema.__dict__['declared_fields'])
        self.assertEqual(total_class_attributes, 3)


