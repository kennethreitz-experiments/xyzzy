# -*- coding: utf-8 -*-

"""
xyzzy.game
~~~~~~~~~~

This module defines the actual game.
"""


class Game(object):
    """The instance of the actual game."""
    def __init__(self):
        self.commands = set()

    def register_command(self, cmd):
        pass

    def lookup_command(self, cmd)
