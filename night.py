"""
晚安
"""
from send_msg import send_msg
from night_msg import get_night_msg
from pet_name import get_pet_name


if __name__ == '__main__':
    send_msg('18739776523', '晚安')
    send_msg('慧宝', [get_night_msg, f'{get_pet_name()}晚安'])
