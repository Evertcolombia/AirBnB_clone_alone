#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            items = {}
            for key, val in FileStorage.__objects.items():
                if type(cls) == str:
                   if cls == val.__class__.__name__:
                       items[key] = val
                else:
                    if cls == val.__class__:
                        items[key] = val
            return items
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            to_delete = next((el for el in self.__objects.keys() if el.split(".")[1] == obj.id), None)
            self.__objects.pop(to_delete)

    def close(self):
        self.reload()

    def get(self, cls, id):
        """Returns the object based on the
        class name and its ID"""
        if cls and id and type(id) == str:
            if type(cls) == str and cls in classes:
                key = cls + '.' + id
            else:
                key = cls.__name__ + '.' + id
            item = self.__objects.get(key, None)
            return item
        else: return None

    def count(self, cls=None):
        """Returns the number of objects in storage
        matching the given class name"""
        total = 0
        if cls:
            total = len(self.all(cls))
        else: 
            total = len(self.__objects)
        return total
        
