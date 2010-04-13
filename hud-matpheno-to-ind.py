"""
Convert a .hud file and a MAT_pheno.txt file to an .ind file.
The .hud file provides the names of the OTUs.
The MAT_pheno.txt file provides the 'case-control' status.
The output file is in eigenstrat format.
"""

import os
import sys

import argparse

def gen_nonempty_stripped_lines(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield line

def get_first(elements):
    for element in elements:
        return element

def main(args):
    # get the names from the .hud file
    names = []
    with open(os.path.expanduser(args.hud)) as fin_hud:
        for line in gen_nonempty_stripped_lines(fin_hud):
            name, rest = line.split(None, 1)
            names.append(name)
    # get case and control status from the matpheno file
    cases = set()
    controls = set()
    with open(os.path.expanduser(args.matpheno)) as fin_matpheno:
        for line in gen_nonempty_stripped_lines(fin_matpheno):
            name, classification = line.split(None, 1)
            if classification == '1':
                cases.add(name)
            elif classification == '2':
                controls.add(name)
            elif classification in ('12', 'null'):
                # skip individuals classified like this
                pass
            else:
                msg = 'invalid MAT_pheno classification: ' + classification
                raise Exception(msg)
    # write the .ind file contents
    for name in names:
        gender = 'U'
        classification = 'Ignore'
        if name in cases:
            classification = 'Case'
        elif name in controls:
            classification = 'Control'
        row = [name, gender, classification]
        print '\t'.join(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hud', required=True,
            help='a .hud file')
    parser.add_argument('--matpheno', required=True,
            help = 'a MAT_pheno.txt file')
    args = parser.parse_args()
    main(args)
