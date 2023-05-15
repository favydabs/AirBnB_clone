#!/usr/bin/python3
"""
Defines the User class and,
Initializes attributes that represents a User
"""
from models.base_model import BaseModel


class User(BaseModel):

    """ class attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
