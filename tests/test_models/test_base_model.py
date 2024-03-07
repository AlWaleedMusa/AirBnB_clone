#!/usr/bin/env python3

"""Defines unittest for models/base_model.py.

Unittest classes:
    TestBaseModel
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):

    def test_initialization_with_args(self):
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        base_model = BaseModel(id="123",
                               created_at=now,
                               updated_at=now)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(base_model.created_at.strftime
                         ("%Y-%m-%dT%H:%M:%S.%f"),now)
        self.assertEqual(base_model.updated_at.strftime
                         ("%Y-%m-%dT%H:%M:%S.%f"), now)

    def test_initialization_without_args(self):
        now = datetime.datetime.now()
        base_model = BaseModel()
        id = base_model.id
        self.assertNotEqual(base_model.id, "123")
        self.assertEqual(base_model.id, id)
        self.assertEqual(base_model.created_at, now)
        self.assertEqual(base_model.updated_at, now)

    def test_str_representation(self):
        base_model = BaseModel(id="123")
        self.assertEqual(str(base_model),
                         "[BaseModel] (123) {'id': '123'}")

    def test_save_method(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at.strftime
        ("%Y-%m-%dT%H:%M:%S.%f")
        base_model.save()
        self.assertNotEqual(base_model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        now = datetime.datetime.now()
        base_model = BaseModel(id="123", created_at=now, updated_at=now)
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], '123')
        self.assertEqual(base_model_dict['created_at'], now.isoformat())
        self.assertEqual(base_model_dict['updated_at'], now.isoformat())


if __name__ == '__main__':
    unittest.main()
