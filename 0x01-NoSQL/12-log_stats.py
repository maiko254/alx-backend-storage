#!/usr/bin/env python3
"""Module filtering nginx logs in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    coll = db.nginx

    print(f"{coll.count_documents({})} logs \nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = len(list(coll.find({'method': method})))
        print(f"\tmethod {method}: {count}")

    filter = {'method': 'GET', 'path': '/status'}
    status_check_count = len(list(coll.find(filter)))
    print(f"{status_check_count} status check")
