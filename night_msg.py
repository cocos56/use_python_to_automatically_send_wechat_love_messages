"""
晚安文案
"""
from base import get_random_item

night_messages = [
    '在看得见的地方，我的眼睛和你在一起；在看不见的地方，我的心和你在一起。',
    '虽然我遇见你很晚，但阳光甚好，来日方长，我想陪你很久很久。',
    '你眼中有浓浓的夜，挂起着盈盈的月，倾洒进我的心房，让我日思，夜也难忘。'
]


def get_night_msg():
    """
    获取晚安文案
    :return: 晚安文案
    """
    return get_random_item(night_messages)
