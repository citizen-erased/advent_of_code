import os
import sys

def _read_path(input_filename):
    return os.path.join(os.path.dirname(sys.argv[0]), input_filename)


def read_single_line(input_filename):
    with open(_read_path(input_filename)) as f:
        return [line.strip() for line in f][0]


def read_lines(input_filename):
    with open(_read_path(input_filename)) as f:
        return [line.strip() for line in f]


def read_map(input_filename):
    with open(_read_path(input_filename)) as f:
        map = [[c for c in line.strip()] for line in f]
        w, h = len(map[0]), len(map)
        return map, w, h