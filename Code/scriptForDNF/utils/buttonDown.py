"""
@File buttonDown.py
@Contact cmrhyq@163.com
@License (C)Copyright 2022-2025, AlanHuang
@Modify Time 2023/2/23 17:38
@Author Alan Huang
@Version 0.0.1
@Description None
"""
import win32con
import win32api
import time


# key: 按键对应的键值
# release_time: 等待时间
def button_down(key, release_time):
    # 按下按键
    win32api.keybd_event(key, 0, 0, 0)
    time.sleep(release_time)
    # 这行代码代表按键建松开
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
