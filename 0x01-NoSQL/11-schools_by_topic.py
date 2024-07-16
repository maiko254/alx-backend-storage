#!/usr/bin/env python3
"""Module searching a document with a given topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds document in a school collection with the given topic

    Args:
        mongo_collection: A PyMongo collection object
        topic: topic to search for in documents in the collection

    Returns:
        List of schools offering a given topic
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass
