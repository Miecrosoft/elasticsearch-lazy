#!/usr/bin/env python3
import sys
import argparse

# from elasticsearch import Elasticsearch
import setmap

parser = argparse.ArgumentParser()
parser.add_argument("-H", help="HOST")
parser.add_argument("-P", help="PORT")
args = parser.parse_args()

if args.H is None:
  print ("localhost")
else:
  print (args.H)

if args.P is None:
  print ("9200")
else:
  print (args.P)