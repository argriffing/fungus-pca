"""
This is a wrapper for eigenstrat.
"""

import subprocess
from subprocess import PIPE

import argparse

def run_smartpca(name):
    d = {
            'i' : 'geno',
            'j' : 'pheno',
            'p' : 'pca',
            'o' : 'chisq'}
    cmd = ['eigenstrat']
    for k, v in d.items():
        flag = '-' + k
        filename = name + '.' + v
        cmd.extend([flag, filename])
    p = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
    return p.communicate()

def main(args):
    out, err = run_smartpca(args.name)
    print out
    print err

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='base name of the project')
    args = parser.parse_args()
    main(args)
