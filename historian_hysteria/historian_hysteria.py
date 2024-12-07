#!/usr/bin/env python

# Import built-ins
import copy
import os
from typing import Iterable

# Globals
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_ROOT = os.path.dirname(SCRIPT_PATH)
PROJECT_ROOT = os.path.dirname(SCRIPT_ROOT)


def read_data_file(filename: str) -> str:
    _data_file = os.path.join(PROJECT_ROOT, "data", filename)
    with open(_data_file, mode="r") as _file:
        return _file.read()


def extract_columns(corpus: str) -> tuple[list, list]:
    _left_column: list[int] = []
    _right_column: list[int] = []
    for _line in corpus.splitlines():
        _left_datum, _right_datum = _line.strip().split()
        _left_column.append(int(_left_datum))
        _right_column.append(int(_right_datum))
    return _left_column, _right_column


def create_sorted_pairs(first_column: list[int],
                        second_column: list[int]
                       ) -> Iterable[tuple[int, int]]:
    return zip(sorted(copy.deepcopy(first_column)),
               sorted(copy.deepcopy(second_column)))


def sum_distance_differences(pairs: Iterable[tuple[int, int]]) -> int:
    return sum(abs(_left_datum - _right_datum)
               for _left_datum, _right_datum in pairs)


contents = read_data_file("distances.txt")
left_column, right_column = extract_columns(contents)
sorted_pairs = create_sorted_pairs(left_column, right_column)
total_difference = sum_distance_differences(sorted_pairs)

print("\nPart 1\n------")
print("The total difference of distances between lists is equal to "
      f"{total_difference:,} units.")
