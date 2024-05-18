#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any).
            **kwargs (dict): Key/value pairs of attributes.
        """
        dtform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes a key __class__ representing
        the class name of the object.
        """
        var_dict = self.__dict__.copy()
        var_dict["created_at"] = self.created_at.isoformat()
        var_dict["updated_at"] = self.updated_at.isoformat()
        var_dict["__class__"] = self.__class__.__name__
        return var_dict

    def __str__(self):
        """Print the str representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
