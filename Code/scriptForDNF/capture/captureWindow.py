"""
@File captureWindow.py
@Contact cmrhyq@163.com
@License (C)Copyright 2022-2025, AlanHuang
@Modify Time 2023/2/25 23:30
@Author Alan Huang
@Version 0.0.1
@Description None
"""
import win32api
import win32gui
import win32con

from utils.button import button_down
from enums.buttonEnum import LeftKeyBoard, RightKeyBoard, ControlKeyBoard, FunctionKeyBoard


def match_windows(win_title):
    """
    查找指定窗口
    :param win_title: 窗口名称
    :return: 句柄列表
    """

    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            win_text = win32gui.GetWindowText(hwnd)
            # 模糊匹配
            if win_text.find(win_title) > -1:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)  # 列出所有顶级窗口，并传递它们的指针给callback函数
    print(hwnds)
    return hwnds


def capture_window(window_name):
    assert window_name, "窗口名不能为空！"
    handle = match_windows(window_name)

    window = win32gui.FindWindow(None, window_name)
    window_operate = win32gui.FindWindowEx(window, None, "operate", None)

    if handle:
        win32gui.ShowWindow(handle[0], win32con.SW_SHOWNORMAL)  # SW_SHOWNORMAL 默认大小，SW_SHOWMAXIMIZED 最大化显示
        win32gui.SetForegroundWindow(handle[0])
        button_down(ControlKeyBoard.left_arrow.value, 5)
