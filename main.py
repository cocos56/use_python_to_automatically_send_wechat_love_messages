"""
自动向女朋友的微信发送天气预报
"""
import time
from datetime import datetime
from urllib.request import urlopen
from urllib.error import HTTPError

import pyautogui
import pyperclip


def get_weather(area_code):
    """
    获取天气信息
    """
    try:
        with urlopen(f'https://weather.mipang.com/tianqi-{area_code}') as html:
            html_read = bytes.decode(html.read()).replace("\n", "").replace("\r", "")
            return html_read.split("row row1")[1].split(">")[1].split("<")[0]
    except HTTPError:
        time.sleep(1)
        return get_weather(area_code)


def sent_msg(name, msg):
    """
    发送信息
    :param name: 联系人名字（备注）
    :param msg: 待发送的信息，支持元组（多条信息）、字符串和列表（单条信息）
    """
    # 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    time.sleep(1)
    # 查找联系人
    pyautogui.hotkey("ctrl", "f")
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    # 粘贴并发送信息
    if not type(msg) == tuple:
        msg = tuple([msg])
    for m in msg:
        if type(m) == str:
            pyperclip.copy(m)
        elif type(m) == list:
            pyperclip.copy('\n'.join(m))
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('Enter')
    time.sleep(1)
    # 关闭微信
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)


if __name__ == '__main__':
    # pylint: disable=C0103
    yu = 0
    last_day = 0
    while True:
        time.sleep(1)
        now = datetime.now()
        if last_day == now.day:
            continue
        if not now.hour == 9:
            continue
        if not now.minute == 12:
            continue
        yu += 1
        sent_msg("18739776523", ([get_weather(2093), '咸阳'], "爱你（づ￣3￣）づ╭❤～"))
        print("又过去1天：合计守护", yu, "天")
        last_day = now.day
