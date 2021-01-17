from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.findbestmatch import find_best_match
from pywinauto.keyboard import send_keys
import time
import keyboard
import os
import sys
from psutil import process_iter


class SelectAddress():
    "发送微信"

    "addressee:微信名称"

    def __init__(self, addressee):

        self.addressee = addressee

    def weixin(self):
        app = Application(backend='uia').connect(process=get_pid("WeChat.exe"))
        win_main_Dialog = app.window(class_name='WeChatMainWndForPC')
        win_main_Dialog.restore()

        time.sleep(0.5)
        pane = win_main_Dialog.child_window(best_match=self.addressee)
        rect = pane.rectangle()
        cx = int((rect.left+rect.right)/2)
        cy = int((rect.top + rect.bottom)/2)
        mouse.click(button='left', coords=(cx, cy))


def get_pid(name):
    PID = process_iter()

    pid_num = 0
    for pid_temp in PID:
        pid_dic = pid_temp.as_dict(attrs=['pid', 'name'])
        if pid_dic['name'] == name:
            pid_num = pid_dic['pid']
            break

    return pid_num
