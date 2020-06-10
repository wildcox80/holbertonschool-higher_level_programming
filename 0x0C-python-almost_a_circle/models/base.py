#!/usr/bin/python3
"""
    1-base.py: Model class Base
    Wilder Rincon : 1588@holbertonschool.com
"""
from random import random
import json
import csv


class Base:
    """
        Define Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize public instance attr id

        Args:
            id ([int], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method return JSON with list dictionaries """

        if not list_dictionaries or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string representation of objects in list to file

            Description:
                Writes JSON string representation of objects
                in list_objs to file <Class name>.json

            Parameter:
                list_objs: list of objects
        """
        write_list = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                write_list.append(obj.to_dictionary())
        write_list = Base.to_json_string(write_list)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(write_list)

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return instance with all attributes its seted """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        else:
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ Return list of instances from file
            filename is <Class name>.json
        """
        try:
            filename = "{}.json".format(cls.__name__)
            with open(filename, 'r') as f:
                objs = Base.from_json_string(f.read())
                instances = [cls.create(**obj) for obj in objs]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a representations of objects in list to CSV file
        Description"
            Write CSV representation of objects in list_objs to file
            <Class name>.csv
            Parameter:
                list_objs: list of objects
        """
        if cls.__name__ == "Rectangle":
            attrs = ['id', 'width', 'height', 'x', 'y']
        else:
            attrs = ['id', 'size', 'x', 'y']
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as csvf:
            if list_objs is not None:
                writer = csv.DictWriter(csvf, fieldnames=attrs)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                writer = csv.writer(csvf)
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """Return list of instances from file
        filename is <Class name>.csv
        """
        try:
            filename = "{}.csv".format(cls.__name__)
            with open(filename, newline='') as csvf:
                reader = csv.DictReader(csvf)
                obj_list = []
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    obj_list.append(row)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []
