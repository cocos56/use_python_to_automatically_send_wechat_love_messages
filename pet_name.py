"""
爱称
"""
from base import get_random_item

pet_names = [
    '宝贝儿',
    '亲爱的',
    '宝宝',
    '慧宝',
    '老婆',
    '媳妇儿',
    '小慧'
]


def get_pet_name():
    return get_random_item(pet_names)
