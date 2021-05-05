#!/usr/bin/env python3
"""
    List all documents in Python
"""


def list_all(mongo_collection) -> list:
    """
        function that lists all documents in a collection.
    """
    docs = mongo_collection.find()
    if docs.count() == 0:
        return []
    else:
        return docs
