import os
import sys

def _read_path(input_filename):
    return os.path.join(os.path.dirname(sys.argv[0]), input_filename)


def read_text(input_filename):
    with open(_read_path(input_filename)) as f:
        return f.read().replace("\r\n", '\n')


def read_single_line(input_filename):
    with open(_read_path(input_filename)) as f:
        return [line.strip() for line in f][0]


def read_lines(input_filename, strip=True):
    with open(_read_path(input_filename)) as f:
        if strip:
            return [line.strip() for line in f]
        else:
            return [line for line in f]


def read_map(input_filename):
    with open(_read_path(input_filename)) as f:
        map = [[c for c in line.strip()] for line in f]
        w, h = len(map[0]), len(map)
        return map, w, h

def parse_map(text):
    map = [[c for c in line.strip()] for line in text.splitlines()]
    w, h = len(map[0]), len(map)
    return map, w, h

def split_input_lines_into_sections(lines):
    sections, section = [], []

    for line in lines:
        if line.strip() == "":
            sections.append(section)
            section = []
        else:
            section.append(line)
    
    if section:
        sections.append(section)

    return sections