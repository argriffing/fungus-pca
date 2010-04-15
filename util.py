"""
Utility functions.
"""

def gen_nonempty_stripped_lines(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield line

def get_first(elements):
    for element in elements:
        return element
