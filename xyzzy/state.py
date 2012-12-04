# -*- coding: utf-8 -*-

"""
xyzzy.state
~~~~~~~~~~~

Thsi module defines the save state class and persistience
"""

from . import defaults

class GameState(object):
    """Interactive GameState."""
    def __init__(self, arg):
        self.data = DEFAULTS.copy()
        self.events
        self.inventory =
        # self.location

    @classmethod
    def restore(cls, fo):
        g = cls()
        g.data

    def get(self, key, default):


    def set(self, key, value)