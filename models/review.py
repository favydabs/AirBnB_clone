#!/usr/bin/python3
"""
Defines Review class and,
Initializes attributes that represents Review
"""

from models.base_model import BaseModel


class Review(BaseModel):

    """ review attributes """
    place_id = ""
    user_id = ""
    text = ""
