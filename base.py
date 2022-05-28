"""
基层
"""
from random import randint


def get_random_item(items):
    return items[randint(0, len(items) - 1)]
