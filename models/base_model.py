#!/usr/bin/python3
"""
Defines the base model
"""
import uuid
from datetime import datetime
from models import storage

time_format = '%Y-%m-%dT%H:%M:%S.%f'  # Sets time format to a variable


class BaseModel:
    """
    Defines attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel class
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time_format)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            new_dict.pop('_sa_instance_state', None)
        return new_dict

 def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)