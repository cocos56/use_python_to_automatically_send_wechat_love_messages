"""
自动向女朋友的微信发送天气预报
"""
import time
from datetime import datetime
from urllib.request import urlopen

import pyautogui
import pyperclip


def open_wechat():
    """
    使用快捷键打开微信界面
    """
    pyautogui.hotkey('ctrl', 'alt', 'w')
    time.sleep(1)


def get_weather():
    """
    获取天气信息
    """
    with urlopen('https://weather.mipang.com/tianqi-2093') as html:
        html_read = bytes.decode(html.read()).replace("\n", "").replace("\r", "")
        info = html_read.split("row row1")[1].split(">")[1].split("<")[0]
        res = info + "\n咸阳"
        return res


def chat_who(who_name):
    """
    搜索联系人并进入与目标联系人的聊天界面
    :param who_name: 联系人备注
    """
    pyautogui.hotkey("ctrl", "f")
    pyperclip.copy(who_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)


def sent_msg(msg):
    """
    发送信息
    :param msg: 待发送的信息
    """
    pyperclip.copy(str(msg))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('Enter')


if __name__ == '__main__':
    # pylint: disable=C0103
    yu = 0
    last_day = 0
    while True:
        time.sleep(30)
        now = datetime.now()
        if last_day == now.day:
            continue
        if not now.hour == 7:
            continue
        yu += 1
        open_wechat()
        chat_who("慧宝")
        sent_msg(get_weather())
        sent_msg("爱你（づ￣3￣）づ╭❤～")
        print("又过去1天：合计守护", yu, "天")
        lastDay = now.day
