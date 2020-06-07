#!/usr/bin/python3
""" unit test for file base.py """
import unittest
from models.base import Base


class TestTask_One(unittest.TestCase):
    """ unit testing class Base task 1. Base class """

    def test_empty_arg(self):
        """ check empty argument send to function """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(None).id, 4)        

    def test_send_func(self):
        """ check with argument send to function"""
        self.assertEqual(Base(13).id, 13)
        self.assertEqual(Base('s').id, 's')
        self.assertEqual(Base("holberton").id, "holberton")

    def test_send_more_arg(self):
        """ check send more of one argument to funtion """
        with self.assertRaises(TypeError):
            Base(5, 4)
        with self.assertRaises(TypeError):
            Base([1, 3], [3, 5])

    # def test_check_increment(self):
    #     """ check if value id not is incremented after error """
    #     Base._Base__nb_objects = 0
    #     base = Base()                   
    #     self.assertEqual(base.id, 1)

    def test_validate_private_attr(self):
        """ validate private attribute for __nb_objects """
        b = Base(25)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)
    

if __name__ == "__main__":
    unittest.main()
