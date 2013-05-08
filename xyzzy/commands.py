# -*- coding: utf-8 -*-

"""
xyzzy.commands
~~~~~~~~~~~~~~

This module contains the gameplay commands.
"""

from .game import game

# save, restore, get

class Command(object):
    """docstring for Command"""
    def __init__(self):
        """Registers handler callback for command.
        If a string is provided, it will simply be printed to the player
        session.
        """
        self.aliases = []

    def run(self, state):
        """Executes the command. Modifies state. Returns player message."""

        raise NotImplementedError

@game.register_command
class GetCommand(Command):
    """Get an object from environment, place in inventory."""
    aliases = ['steal', 'take', 'fetch', 'grab']

    def run(self, state):
        return 'You thief!'

