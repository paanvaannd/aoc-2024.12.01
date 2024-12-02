#!/usr/bin/env python

# Import built-ins
import os

script_path = os.path.abspath(__file__)
script_root = os.path.dirname(script_path)
project_root = os.path.dirname(script_root)

data_file = os.path.join(project_root, "data", "")
with open(data_file) as data:
    pass
