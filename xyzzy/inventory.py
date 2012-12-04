# -*- coding: utf-8 -*-
"""
xyzzy.inventory
~~~~~~~~~~~~~~~

This module contains the ba
"""

from random import choice

class BaseItem(object):
    """The base class for an item in inventory."""
    def __init__(self):
        pass

    def __repr__(self):
        return '<BaseItem at 0x%x>' % id(self)

class ContainerItem(BaseItem):
    """An item in inventory that contains other items."""

    def __init__(self):
        super(ContainerItem, self).__init__()
        self.items = []

    def add_item(self, item):
        # if self.vali
        self.items()

    def remove_item(self, item):
        pass

    def pop(self, index=-1):
        """Removes the item from the top of the container, then returns it."""

        return self.items.pop(index)

    def rand_pop(self):
        """Removes a random item from the container, then returns it."""

        i = choice(range(len(self.items)))
        return self.pop(i)
