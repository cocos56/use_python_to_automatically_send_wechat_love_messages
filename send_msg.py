"""
发送信息
"""
from time import sleep
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
            html_read = bytes.decode(html.read()).replace('\n', '').replace('\r', '')
            return html_read.split('row row1')[1].split('>')[1].split('<')[0]
    except HTTPError:
        sleep(1)
        return get_weather(area_code)


def send_msg(name, msg):
    """
    发送信息
    :param name: 联系人名字（备注）
    :param msg: 待发送的信息，支持列表（多条信息）、字符串（单条信息单行）和元组（单条信息多行）
    """
    # 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    sleep(1)
    # 查找联系人
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.hotkey('Enter')
    sleep(1)
    # 粘贴并发送信息
    if not isinstance(msg, list):
        msg = [msg]
    for i in msg:
        if isinstance(i, str):
            pyperclip.copy(i)
        elif isinstance(i, tuple):
            pyperclip.copy('\n'.join(i))
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('Enter')
    sleep(1)
    # 关闭微信
    pyautogui.hotkey('alt', 'f4')
    sleep(1)
