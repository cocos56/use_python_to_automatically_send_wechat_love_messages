"""
基层
"""
from random import randint


def get_random_item(items):
    """
    从多个元素中随机获取其中的某一个元素
    :param items: 多个元素
    :return: 多个元素中的某一个元素
    """
    return items[randint(0, len(items) - 1)]
