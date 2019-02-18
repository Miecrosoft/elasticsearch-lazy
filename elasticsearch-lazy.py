#!/usr/bin/env python3
import argparse
import json
from elasticsearch import Elasticsearch
obj = object

parser = argparse.ArgumentParser()
parser.add_argument("-H", help = "HOST localhost as default", default="localhost")
parser.add_argument("-P", help = "PORT 9200 as default", default="9200")
parser.add_argument("-a", help = "Action executed such as indices, cluster, etc")
parser.add_argument("-e", help = "Action executed such as status, create, delete, etc")
parser.add_argument("-n", help = "Name")
args = parser.parse_args()

es = Elasticsearch(host = args.H, port = args.P)

def close(api, param):
  res = api.close(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def create(api, param):
  res = api.create(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def delete(api, param):
  res = api.delete(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def exists(api, param):
  res = api.exists(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def flush(api, param):
  res = api.flush(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def get_mapping(api, param):
  res = api.get_mapping(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def get_settings(api, param):
  res = api.get_settings(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def open(api, param):
  res = api.open(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

def stats(api, param):
  res = api.stats(index = param)
  print(json.dumps(res, indent = 2, sort_keys = False))

if args.a == "indices":
  obj = es.indices

if args.e == "close":
  close(obj, args.n)
elif args.e == "create":
  create(obj, args.n)
elif args.e == "delete":
  delete(obj, args.n)
elif args.e == "exists":
  exists(obj, args.n)
elif args.e == "flush":
  flush(obj, args.n)
elif args.e == "get_mapping":
  get_mapping(obj, args.n)
elif args.e == "get_settings":
  get_settings(obj, args.n)
elif args.e == "open":
  open(obj, args.n)
elif args.e == "stats":
  stats(obj, args.n)
