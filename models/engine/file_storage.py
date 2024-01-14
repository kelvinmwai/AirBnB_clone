#!/usr/bin/python3
"""
    Definition for class FileStorage Module
"""
import json


class FileStorage:
    """
        Serialize and deserialize instances to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self, classes=None):
        self.classes = classes

    def all(self):
        """
            Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Set new obj into __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects into JSON file
        """
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        Reload the file and deserializes JSON into __objects
        """
        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                objects_dict = json.load(fd)
                for key, val in objects_dict.items():
                    class_name = val["__class__"]
                    model_class = self.classes.get(class_name)
                    if model_class:
                        self.__objects[key] = model_class(**val)
        except FileNotFoundError:
            pass

