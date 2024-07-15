#!/usr/bin/env python3
"""
Module that inserts a document into a collection in MongoDB
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection(passed in as argument) based on
    key-word arguments

    Args:
        mongo_collection: A PyMongo collection objects
        kwargs: keyword arguments to be inserted in collection

    Returns:
        _id(Unique Object Identifier) of the new document inserted
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id


if __name__ == "__main__":
    pass
