#!/usr/bin/pyton3
"""User module"""
from models import BaseModel


class User(BaseModel):
    """define User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
