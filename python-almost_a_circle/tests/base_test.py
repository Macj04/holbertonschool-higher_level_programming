#!/usr/bin/python3
"""Test module for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test cases for Base class"""

    def test_is_instance(self):
        """Check if it creates an instance of Base"""
        instance = Base()
        self.assertTrue(isinstance(instance, Base))

    def test_id_custom(self):
        """Check if id is set correctly with custom value"""
        instance = Base(4)
        self.assertEqual(instance.id, 4)

    def test_id_default(self):
        """Check if id is set correctly with default value"""
        instance = Base()
        self.assertEqual(instance.id, 1)

    def test_to_json_string(self):
        """Check if it converts a list of dictionaries to JSON string"""
        list_dicts = None
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, "[]")

        empty_list = []
        json_string = Base.to_json_string(empty_list)
        self.assertEqual(json_string, "[]")

    def test_save_to_file(self):
        """Check if it saves objects to a file in JSON format"""
        rectangle = Rectangle(2, 3)
        square = Square(4)

        Base.save_to_file([rectangle, square])


    def test_from_json_string(self):
        """Check if it converts a JSON string to a list of dictionaries"""
        empty_json_string = "[]"
        empty_dict_list = Base.from_json_string(empty_json_string)
        self.assertEqual(empty_dict_list, [])

        invalid_json_string = "invalid"
        invalid_dict_list = Base.from_json_string(invalid_json_string)
        self.assertEqual(invalid_dict_list, [])

    def test_create(self):
        """Check if it creates objects based on dictionaries"""
        rectangle_dict = {"width": 5, "height": 10}
        rectangle_obj = Base.create(**rectangle_dict)
        self.assertEqual(rectangle_obj.width, 5)
        self.assertEqual(rectangle_obj.height, 10)

        square_dict = {"side": 3}
        square_obj = Base.create(**square_dict)
        self.assertEqual(square_obj.side, 3)

    def test_load_from_file(self):
        """Check if it loads objects from a file"""
        # Create a "Rectangle.json" file with valid content

        loaded_objects = Base.load_from_file()



if __name__ == "__main__":
    unittest.main()

