# -*- coding: utf-8 -*-

"""
xyzzy.commands
~~~~~~~~~~~~~~

This module contains the gameplay commands.
"""


__commands__ = []

def register_command(cmd):
    pass

# save, restore, get


class Command(object):
    """docstring for Command"""
    def __init__(self, handler):
        """Registers handler callback for command.
        If a string is provided, it will simply be printed to the player
        session.
        """
        self.aliases = []
        self.handler = handler

    def run(self, state):
        """Executes the command. Modifies state. Returns player message."""


get = Command(run_command)
get.aliases.extend(['steal', 'take', 'fetch', 'grab'])
