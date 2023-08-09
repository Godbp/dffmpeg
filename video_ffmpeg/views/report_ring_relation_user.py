#!/usr/bin/python
# -*- coding: <encoding name> -*-

import sys
import csv
from pymongo import MongoClient

# arguments = sys.argv
# #
# if len(arguments) == 1:
#     arguments.append(
#         "mongodb://mongosroot:mongosroot@192.168.50.249:30000,192.168.50.248:30000,192.168.50.247:30000/?authSource=admin")
#
# mongo_addr = arguments[1]
# mg_client = MongoClient(mongo_addr, connect=False)
mg_client = MongoClient("mongodb://root:IvGS2VdS5e6DNv^nJcard4NjLrdxRrqv@s-d9jaf4f1afb895f4.mongodb.ap-southeast-5"
                        ".rds.aliyuncs.com:3717,s-d9j7f69f3f270ca4.mongodb.ap-southeast-5.rds.aliyuncs.com:3717/admin",
                        connect=False)
mg = mg_client.de


def get_child(skip, limit):
    match = {"up_id": {"$gt": 0}}
    return mg.user_agent.aggregate([
        {"$match": match},
        {
            "$graphLookup": {
                "from": 'user_agent',
                "startWith": '$_id',
                "connectFromField": 'up_id',
                "connectToField": 'up_id',
                "as": 'children'
            }
        },
        {"$skip": (skip - 1) * limit},
        {"$limit": limit}
    ])


def get_data():
    return mg.user_agent.find_one({"_id": 9968722})


def get_graph():
    first = {}
    page = 0
    limit = 1000
    while True:
        page += 1
        data = get_child(page, limit)
        n = 0
        for i in data:
            n += 1
            if len(i.get("children")) > 0:
                children = []
                for j in i.get("children"):
                    children.append(j.get("_id"))
                first[i.get("_id", 0)] = children
        if n < 10:
            break
        print("select mongo db: ", page)

    return first


def find_cycles(node, visited, path, cycles, graph):
    visited[node] = True
    path.append(node)

    neighbors = graph.get(node, [])
    for neighbor in neighbors:
        if not visited.get(neighbor, 0):
            find_cycles(neighbor, visited, path, cycles, graph)
        elif neighbor in path:
            cycles.append(path[path.index(neighbor):])

    path.pop()
    visited[node] = False


def save_excel(cycles):
    filename = "example.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        for row in cycles:
            csvwriter.writerow(row)

    print("report CSV", filename)


def get_yield():
    graph = get_graph()
    print("get data:", len(graph))

    visited = {node: False for node in graph}
    cycles = []

    for node in graph:
        if not visited[node]:
            find_cycles(node, visited, [], cycles, graph)
    for c in cycles:
        yield c


def del_repeat():
    ys = get_yield()
    cycles2 = []
    for c in ys:
        cc = set(c)
        if len(cycles2) == 0:
            cycles2.append(cc)
            continue
        for cy in cycles2:
            if cc == cy:
                continue
            cycles2.append(cc)
    return cycles2


def mian():
    cycles = del_repeat()
    print("repeat ", len(cycles))
    save_excel(cycles)


if __name__ == "__main__":
    # print(get_data())
    mian()