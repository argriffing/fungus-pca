
import sys

import util

def main():
    values = []
    for line in util.gen_nonempty_stripped_lines(sys.stdin):
        name, gender, status = line.split()
        if status == 'Control':
            v = '0'
        elif status == 'Case':
            v = '1'
        elif status == 'Ignore':
            v = '9'
        else:
            msg = 'Invalid status: ' + status
            raise Exception(msg)
        values.append(v)
    print ''.join(values)

if __name__ == '__main__':
    main()
