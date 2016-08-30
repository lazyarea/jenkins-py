# -*- conding:utf8 -*-

import csv
import json


def load_csv(path, delim=",", quote='"'):
    csv_reader = csv.reader(open(path, "r"), delimiter=delim, quotechar=quote)
    list = []
    for row in csv_reader:
        list = list + row
    return list

def load_json_from_file(path):
    with open(path, 'r') as f:
        obj = json.load(f)
        print (json.dumps(obj))

def write_file(path, data):
    if path == None:
        return

    try:
        f = open(path, 'w')
    except IOError:
        print('cannot open', arg)
    else:
#        print(arg, 'has', len(f.readlines()), 'lines')
        for i in data:
            f.write(str(i))
        f.close()

