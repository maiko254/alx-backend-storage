#!/usr/bin/env python3
"""
Module that lists all documents in a MongoDB collection or returns empty
if none is found
"""


def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection: A PyMongo collection object.

    Returns:
        A list of documents (empty list if no documents exist).
    """
    docs = list(mongo_collection.find())
    return docs


if __name__ == "__main__":
    pass
