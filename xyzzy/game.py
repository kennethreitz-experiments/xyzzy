# -*- coding: utf-8 -*-

"""
xyzzy.game
~~~~~~~~~~

This module defines the actual game.
"""

from . import defaults
from .state import GameState

class Game(object):
    """The instance of the actual game."""
    def __init__(self, state=None):
        self.state = state or GameState()
        self.commands = set()
        self.environments = defaults.environments

    def register_command(self, cmd):
        command = cmd()
        self.commands.add(command)

    def lookup_command(self, cmd):
        """Returns a command from the commands registry."""

    @property
    def is_active(self):
        return self.state.data.get('active')


game = Game()