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
    """for k, v in kwargs.items():
        mongo_collection.insert_one({k: v})"""
    mongo_collection.insert_one({k: v for k, v in kwargs.items()})
    return mongo_collection.insert_id