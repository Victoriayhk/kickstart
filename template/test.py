# *-* coding: utf-8 *-*

import sys
import codecs

input_file = sys.argv[1]
output_file = sys.argv[2]


def array1(n, default_value=None):
    arr = [None for i in range(n)]
    return arr


def array2(n, m, default_value=None):
    arr = [[None for j in range(m)] for i in range(n)]
    return arr


def main(fin):
    # n = int(fin.readline().strip())
    # n, m = map(int, fin.readline().split())
    return "ready to go."


###############################################################################

with codecs.open(input_file, mode="r", encoding='utf-8') as fin:
    with codecs.open(output_file, mode="w", encoding='utf-8') as fout:
        T = int(fin.readline().strip())
        for cas in range(T):
            ans = main(fin)
            fout.write("Case #{0}: {1}\n".format(cas + 1, ans))
        #     out = "Case #%d: %d\n" % (cas + 1, ans)
        #     fout.write(out)
