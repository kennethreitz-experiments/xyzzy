# -*- coding: utf-8 -*-

"""
Adventure!

Usage: adventure [--resume]

"""

from docopt import docopt
from .version import version
from .commands import game

def main():
    args =  docopt(__doc__, version=version)

    if args.get('restore'):
        print 'Loading save state...'
        state = None

    state = None

    while game.is_active:

        get
        exit()


