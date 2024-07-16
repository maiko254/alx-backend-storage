#!/usr/bin/env python3
"""Module filtering nginx logs in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    coll = db.nginx

    print(f"{coll.count_documents({})} logs \nMethods:")
    print(f"    method GET: {coll.count_documents({'method': 'GET'})}")
    print(f"    method POST: {coll.count_documents({'method': 'POST'})}")
    print(f"    method PUT: {coll.count_documents({'method': 'PUT'})}")
    print(f"    method PATCH: {coll.count_documents({'method': 'PATCH'})}")
    print(f"    method DELETE: {coll.count_documents({'method': 'DELETE'})}")
    filter = {'method': 'GET', 'path': '/status'}
    print(f"{coll.count_documents(filter)} status check")
