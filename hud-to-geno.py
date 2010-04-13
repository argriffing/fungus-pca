"""
Convert a .hud genotype file to a .geno genotype file.
"""

import sys

import argparse

def gen_nonempty_stripped_lines(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield line

def main(args):
    for line in gen_nonempty_stripped_lines(sys.stdin):
        name, genotype_string = line.split(None, 1)
        genotypes = ''.join(genotype_string.split())
        print genotypes

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
