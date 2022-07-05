#!/usr/bin/python3

""" File Storage Tests for the City class  """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """ File Storage tests """

    def test_class_name(self):
        """ test if the all func returns the objects private var """
        obj = FileStorage()
        self.assertEqual((obj.__class__).__name__, "FileStorage")

    def test_new(self):
        """ test the instance new """
        file = FileStorage()
        base = BaseModel()
        self.assertEqual(file.new(base), None)

    def test_save(self):
        """ test the instance save """
        obj = FileStorage()
        self.assertEqual(obj.save(), None)

    def test_reload(self):
        """ test the instance reload """
        obj = FileStorage()
        self.assertEqual(obj.reload(), None)

    def test_save_base(self):
        """ test the instance save of the BaseModel class """
        obj = BaseModel()
        self.assertEqual(obj.save(), None)

    def test_init_base(self):
        """ test init of BaseModel """
        obj = BaseModel()
        other = BaseModel()
        obj.name = "Juannito Perez"
        self.assertEqual(other.__init__(obj), None)

    if __name__ == "__main__":
        unittest.main()
