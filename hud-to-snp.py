"""
Convert a .hud genotype file to a .snp file.
The output file is in eigenstrat format.
"""

import sys

import argparse

import util

def main(args):
    line = util.get_first(util.gen_nonempty_stripped_lines(sys.stdin))
    otu_name, genotype_string = line.split(None, 1)
    genotypes = genotype_string.split()
    for i, genotype in enumerate(genotypes):
        name = 'SNP_' + str(i)
        chromosome = '1'
        morgans = '0.0'
        bases = i+1
        row = [name, chromosome, morgans, bases]
        print '\t'.join(str(x) for x in row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    main(args)
