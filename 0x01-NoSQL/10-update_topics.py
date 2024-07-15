#!/usr/bin/env python3
"""Module updating a document in a collection"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.

    Args:
        mongo_collection: A PyMongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.

    Returns:
        None (updates the document in-place).
    """
    mongo_collection.update_many({"name": name}, {'$set': {"topics": topics}})


if __name__ == "__main__":
    pass
