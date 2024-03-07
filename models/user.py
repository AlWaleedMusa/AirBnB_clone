#!/user/bin/env python3

""" class representing User
that inhere from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
