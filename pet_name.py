"""
爱称
"""
from base import get_random_item

pet_names = [
    '宝贝儿', '宝宝', '亲爱的',
    '小慧儿', '慧宝', '霞'
    '媳妇儿', '老婆', '娘子',
    '爱妻', '爱人',
]


def get_pet_name():
    """
    获取爱称
    :return: 爱称
    """
    return get_random_item(pet_names)
