#!/usr/bin/env python3
import argparse
import json
from elasticsearch import Elasticsearch
obj = object

parser = argparse.ArgumentParser()
parser.add_argument("-H", help = "HOST localhost as default", default="localhost")
parser.add_argument("-P", help = "PORT 9200 as default", default="9200")
parser.add_argument("-a", help = "Action executed such as status, create, delete, etc")
parser.add_argument("-e", help = "Action executed such as status, create, delete, etc")
parser.add_argument("-n", help = "Action executed such as status, create, delete, etc")
args = parser.parse_args()

es = Elasticsearch(host = "10.164.5.117", port = "9200")

def create(api, param):
  res = api.create(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def delete(api, param):
  res = api.delete(index=param)
  print(json.dumps(res, indent = 2, sort_keys = False))

if args.a == "indices":
  obj = es.indices

if args.e == "create":
  create(obj, args.n)
elif args.e == "delete":
  delete(obj, args.n)
