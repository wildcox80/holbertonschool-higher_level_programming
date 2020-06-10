#!/usr/bin/python3
""" unit test for file base.py """
import unittest
import pep8
import io
from io import StringIO
import json
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """
    Class containing functions to run
    multiple tests
    """

    def setUp(self):
        """
        function to redirect stdout to check
        outpute of functions relying on print
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything up after running
        setup
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)

    def test_init(self):
        """Initialize with no arguments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_init_param(self):
        """Initialize with id given"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(-1)
        self.assertEqual(b2.id, -1)
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_init_mix(self):
        """Initialize with no id given, id given, no id given"""
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        b3 = Base(8)
        self.assertEqual(b3.id, 8)
        b4 = Base()
        self.assertEqual(b4.id, 6)

    def test_init_toomany(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_init_str(self):
        """Initialize id with string"""
        b1 = Base("123")
        self.assertEqual(b1.id, "123")

    def test_init_dict(self):
        """Initialize id with dictionary"""
        b1 = Base({"123": "456"})
        self.assertEqual(b1.id, {"123": "456"})

    def test_init_tup(self):
        """Initialize id with tuple"""
        b1 = Base((1, ))
        self.assertEqual(b1.id, (1, ))

    def test_init_list(self):
        """Initialize id with list"""
        b1 = Base([1])
        self.assertEqual(b1.id, [1])

    def test_6_from_json_string(self):
        """
        Test to check from json to string
        conversion
        """
        s = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}, \
        {"id": 10, "width": 12, "height": 14, "x": 16, "y": 18}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

    def test_7_from_json_string_empty(self):
        """
        Test to check if it works with
        empty string or none
        """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file_none(self):
        """Test save_to_file() with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            bases = json.load(f)
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_save_to_file_empty(self):
        """Test save_to_file() with empty list"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            bases = json.load(f)
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_load_from_file(self):
        """Test load_from_file with non-existant file"""
        obj = Base.load_from_file()
        self.assertEqual(obj, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_file_csv_none(self):
        """Test save None object to csv file"""
        Base.save_to_file_csv(None)
        with open("Base.csv", "r", newline='') as f:
            bases = Base.load_from_file_csv()
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_save_file_csv_empty(self):
        """Test save empty list to csv file"""
        Base.save_to_file_csv([])
        with open("Base.csv", "r", newline='') as f:
            bases = Base.load_from_file_csv()
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_load_from_file_csv(self):
        """Test loading non-existant file"""
        obj = Base.load_from_file_csv()
        self.assertEqual(obj, [])


if __name__ == "__main__":
    unittest.main()
