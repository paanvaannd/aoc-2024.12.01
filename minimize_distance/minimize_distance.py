#!/usr/bin/env python

# Import built-ins
import os

script_path = os.path.abspath(__file__)
script_root = os.path.dirname(script_path)
project_root = os.path.dirname(script_root)

data_file = os.path.join(project_root, "data", "distances.txt")

left_column:list = []
right_column:list = []
with open(data_file) as data:
    for line in data:
        left_datum, right_datum = line.strip().split()
        left_column.append(int(left_datum))
        right_column.append(int(right_datum))

left_column.sort()
right_column.sort()
total_difference: int = sum(abs(left_datum - right_datum) for left_datum, right_datum in zip(left_column, right_column))

print("\n",
      "Part 1\n",
      "------\n",
      f"The total difference of distances between lists is equal to {total_difference:,} units.")
