"""
Convert a .hud genotype file to a .geno genotype file.
The output file is in eigenstrat format;
it has one line per SNP
and each line has one character per individual.
"""

import sys

import argparse

def gen_nonempty_stripped_lines(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield line

def main(args):
    # for each individual get the genotype of each SNP
    array_per_individual = []
    for line in gen_nonempty_stripped_lines(sys.stdin):
        name, genotypes = line.split(None, 1)
        arr = genotypes.split()
        array_per_individual.append(arr)
    # for each SNP get the genotype for each individual
    array_per_position = zip(*array_per_individual)
    for arr in array_per_position:
        print ''.join(arr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    main(args)
