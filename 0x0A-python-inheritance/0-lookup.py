#!/usr/bin/python3
from inspect import getmembers


def lookup(obj):
    return list(dir(obj))