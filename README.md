# Historian Hysteria

_Advent of Code 2024, Day 1_

**Project status**:

[![UNIX (macOS & Linux)](https://github.com/paanvaannd/aoc-2024.12.01/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/paanvaannd/aoc-2024.12.01/actions/workflows/run_tests.yaml)

## Puzzles

Each puzzle's task is reframed below according to my understanding of the task.

### Puzzle 1

Given an input of distances in unspecified units (i.e., `data/distances.txt`) in 2 columns separated by 3 space characters, calculate the sum of the absolute value of differences between each pair of distances between columns after sorting the columns in ascending order.

### Puzzle 2

Given the same data as in **Puzzle 1**, calculate the similarity index between columns. The similarity index is calculated by iterating over the first column and counting how many occurrences of each value are present in the second column. Each value of the left column is then weighted by multiplying the number of occurrances of each value in the second column by the value of the given number, and then all these weighted values are summed.
