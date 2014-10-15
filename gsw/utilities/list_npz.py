#!/usr/bin/env python
"""
List to stdout the contents of an npz file used in testing.

The filename is the sole command-line argument.
"""

import numpy as np


def list_npz(fname):
    dat = np.load(fname)
    keys = dat.keys()
    keys.sort()
    klens = [len(str(k)) for k in keys]
    klen = max(klens)
    str_fmt = "{0!s:<{klen}} : {1!s:>10}  {2!s:>12}\n"
    slist = [str_fmt.format(k, dat[k].dtype, dat[k].shape, klen=klen)
             for k in keys]
    print(''.join(slist))

if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    list_npz(fname)
