"""
程序入口
"""
from send_msg import get_weather, send_msg


if __name__ == '__main__':
    # pylint: disable=C0103
    send_msg("18739776523", [get_weather(6540), '淮阳'])
    send_msg("慧宝", ([get_weather(2093), '咸阳'], "爱你（づ￣3￣）づ╭❤～", "早上好"))
