#!/usr/bin/env python3
"""
    Change school topics.
"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document based on the name
        - mongo_collection will be the pymongo collection object
        - name (string) will be the school name to update
        - topics (list of strings) will be the list of topics approached in the school
    """
    query = {'name' : name}
    newValues = {'$set' : {'topics': topics}}
    mongo_collection.update_many(query, newValues)
