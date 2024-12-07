#!/usr/bin/env python

# Import built-in modules
from copy import deepcopy
from collections import deque
from itertools import islice

# Import custom modules
import historian_hysteria.historian_hysteria as hh

contents = hh.read_data_file("distances.txt")
left_column, right_column = hh.extract_columns(contents)
sorted_pairs = hh.create_sorted_pairs(left_column, right_column)


def test_columns_are_same_length() -> None:
    assert len(left_column) == len(right_column), \
    "Both columns should be of the same length."


def test_first_ten_values_of_columns() -> None:
    expected_left_column_values = [23238, 94370, 15509, 48816, 31300,
                                   14729, 47167, 18644, 10058, 15802]
    expected_right_column_values = [26034, 90190, 72666, 23909, 40420,
                                    97519, 21596, 62370, 89257, 28645]
    assert left_column[:10] == expected_left_column_values, \
    "The 1st 10 values of the left column should match the expected values."
    assert right_column[:10] == expected_right_column_values, \
    "The 1st 10 values of the right column should match the expected values."


def test_first_ten_sorted_pairs() -> None:
    expected_pairs = [(10058, 10017), (10076, 10170),
                      (10094, 10207), (10126, 10266),
                      (10231, 10375), (10342, 10443),
                      (10427, 10616), (10551, 10729),
                      (10612, 10758), (10638, 10985)]
    _test_sorted_pairs = deepcopy(sorted_pairs)
    assert list(islice(_test_sorted_pairs, 10)) == expected_pairs, \
    "The 1st 10 values of the sorted pairs should match the expected values."


def test_left_column_is_descending() -> None:
    _sorted_pair_deque = deque(deepcopy(sorted_pairs))
    _first_pair = _sorted_pair_deque.popleft()
    _last_pair = _sorted_pair_deque.pop()
    assert _first_pair[0] == min(left_column), \
    "1st value of the 1st pair is the minimum value in the left list."
    assert _last_pair[0] == max(left_column), \
    "1st value of the last pair is the maximum value in the left list."


def test_right_column_is_descending() -> None:
    _sorted_pair_deque = deque(deepcopy(sorted_pairs))
    _first_pair = _sorted_pair_deque.popleft()
    _last_pair = _sorted_pair_deque.pop()
    assert _first_pair[1] == min(right_column), \
    "1st value of the 1st pair is the minimum value in the right list."
    assert _last_pair[1] == max(right_column), \
    "1st value of the last pair is the maximum value in the right list."


def test_sum_distance_differences() -> None:
    assert hh.sum_distance_differences(sorted_pairs) == 2769675, \
    "Sum of differences matches expected value."
