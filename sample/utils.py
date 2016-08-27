# -*- conding:utf8 -*-

import json

def load_json_from_file(path):
    with open(path, 'r') as f:
        obj = json.load(f)
        print (json.dumps(obj))
