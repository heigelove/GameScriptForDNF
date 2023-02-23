"""
@File test.py
@Contact cmrhyq@163.com
@License (C)Copyright 2022-2025, AlanHuang
@Modify Time 2023/2/23 14:13
@Author Alan Huang
@Version 0.0.1
@Description None
"""
import win32con
import win32gui
import win32ui
import win32api
import time

"""
window_name: the name of the window - window title name
file_name:  the name of the file path
"""


def input_word_to_txt(window_name, file_name):
    # 打开变量 file_name的文件
    ret = win32api.ShellExecute(1, "open", file_name, '', '', 1)
    print("opening")
    time.sleep(2)
    # 查找窗口句柄，根据变量 window_name来查找，window_name的值要与标题完全一致
    handle = win32gui.FindWindow(None, window_name)
    # 用上一步找到的句柄查找输入的窗口，由于是编辑，所以窗口对应的参数是EDIT
    handle_edit = win32gui.FindWindowEx(handle, None, "EDIT", None)

    menu = win32gui.GetMenu(handle)
    # 找到窗口对应菜单
    sub_menu = win32gui.GetSubMenu(menu, 0)

    word = ['北国风光，千里冰封，万里雪飘。',
            '望长城内外，惟余莽莽；大河上下，顿失滔滔。',
            '山舞银蛇，原驰蜡象，欲与天公试比高。',
            '须晴日，看红装素裹，分外妖娆。',
            '江山如此多娇，引无数英雄竞折腰。',
            '惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。',
            '一代天骄，成吉思汗，只识弯弓射大雕。',
            '俱往矣，数风流人物，还看今朝。',
            '《沁园春·雪》']
    for index, i in enumerate(word):
        for ch in i:
            # 向输入的窗口输入字符
            win32gui.SendMessage(handle_edit, win32con.WM_CHAR, ord(ch), 0)
            time.sleep(0.05)

        # 写完一行以后，模拟键盘输入Enter键，进行换行，Enter键对应的键值是13
        win32api.keybd_event(13, 0, 0, 0)
        time.sleep(0.05)
        # 这行代码代表Enter建松开
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 根据上面代码找到的菜单获取保存按钮的索引值，记事本保存按钮，从0开始计数正好是第3个。
    button_id = win32gui.GetMenuItemID(sub_menu, 3)
    # 保存输入的内容
    win32gui.PostMessage(handle, win32con.WM_COMMAND, button_id, 0)
    # 关闭窗口
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


if __name__ == '__main__':
    input_word_to_txt("1.txt - 记事本", "G:\\1.txt")
