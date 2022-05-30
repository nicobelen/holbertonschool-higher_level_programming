#!/usr/bin/python3
"""comment 1"""


class MyInt(int):
    """myint"""

    def __eq__(self, other):
        """define eq"""
        return False

    def __ne__(self, other):
        """define ne"""
        return True
