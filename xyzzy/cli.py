# -*- coding: utf-8 -*-

"""
Adventure!

Usage: adventure [--resume]

"""

from docopt import docopt
from .version import version

def main():
    args =  docopt(__doc__, version=version)

    if args.get(''):
        print 'Loading save state...'