import os


class DDA_column:
    def __init__(self, name, type, time_format=None, description=None, cid=None):
        self.name = name
        self.type = type
        self.time_format = time_format
        self.description = description
        self.cid = cid
