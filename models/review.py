#!/usr/bin/env python3

""" class representing Review
that inhere from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
