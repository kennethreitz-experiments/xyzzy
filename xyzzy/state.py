# -*- coding: utf-8 -*-

"""
xyzzy.state
~~~~~~~~~~~

Thsi module defines the save state class and persistience
"""

from . import defaults

class GameState(object):
    """Interactive GameState."""
    def __init__(self):
        self.data = defaults.data.copy()
        self.events = defaults.events.copy()
        self.inventory = defaults.inventory.copy()

    @classmethod
    def restore(cls, fo):
        g = cls()
        g.data

    def get(self, key, default):
        return

    # def set(self, key, value)