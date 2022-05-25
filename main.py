import time
from urllib.request import urlopen

import pyautogui
import pyperclip


def open_wechat():
    pyautogui.hotkey('ctrl', 'alt', 'w')
    time.sleep(1)


def get_weather():
    html = urlopen('https://weather.mipang.com/tianqi-2093')
    html_read = bytes.decode(html.read()).replace("\n", "").replace("\r", "")
    print(html_read)

    TIME = html_read.split("row row1")[1].split(">")[1].split("<")[0]
    print(TIME)
    # TMP = html_read.split("sab1")[1].split(">")[1].split("<")[0]
    # WIND = html_read.split("sab2")[1].split(">")[1].split("<")[0]
    #
    # LOVE = TIME + "\n合肥" + WIND + "温度是" + TMP
    LOVE = TIME + "\n咸阳"
    return LOVE


def chat_who(who_name):
    pyautogui.hotkey("ctrl", "f")
    pyperclip.copy(who_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)


def sent_msg(msg):
    pyperclip.copy(str(msg))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('Enter')


if __name__ == '__main__':
    YU = 0
    while True:
        NOW = str(time.strftime('%H%M', time.localtime()))
        print(NOW)
        if '10' in NOW:
            YU += 1
            open_wechat()
            chat_who("慧宝")
            sent_msg(get_weather())
            sent_msg("爱你（づ￣3￣）づ╭❤～")
            print("又过去1天：合计守护", YU, "天")
            time.sleep(86000)
