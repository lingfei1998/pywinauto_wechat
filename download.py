from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.findbestmatch import find_best_match
from pywinauto.keyboard import send_keys
import time
import keyboard


class Downloading():
    "下载文件并进行保存"
    "apppath:应用路径"
    "doc_name:文档名称"

    def __init__(self, appPath, doc_name):
        self.appPath = appPath
        self.doc_name = doc_name

    def tecentdocs(self):
        # 下载腾讯文档文件
        app = Application(backend='uia').start(self.appPath)  # 启动腾讯文档
        main_Dialog = app.window(class_name="Chrome_WidgetWin_1")
        main_Dialog.restore()
        time.sleep(1)
        pane = main_Dialog.child_window(best_match=self.doc_name)
        rect = pane.rectangle()
        cx = int((rect.left+rect.right)/2)
        cy = int((rect.top + rect.bottom)/2)
        mouse.click(button='left', coords=(cx, cy))
        time.sleep(1)
        main_Dialog2 = app[self.doc_name]  # 文档窗口
        button = main_Dialog2.child_window(best_match="分享")  # 找到分享键
        time.sleep(1)

        rect = button.rectangle()
        rect.left = rect.left-200
        rect.right = rect.right-247
        cx = int((rect.left+rect.right)/2)
        cy = int((rect.top + rect.bottom)/2)
        time.sleep(6)
        mouse.click(button='left', coords=(cx, cy))  # 通过分享键位置点击菜单栏

        mouse.move(coords=(cx+10, cy+150))
        time.sleep(0.5)
        mouse.click(button='left', coords=(cx-120, cy+160))
        time.sleep(5)
        date = time.strftime("%m.%d ", time.localtime())
        self.filename = self.doc_name+"_"+str(date)+".xlsx"
        keyboard.write(self.filename)
        keyboard.send('alt+s')  # 保存

        time.sleep(2)
        app.kill()

    def copy_docs(self):
        app = Application(backend='uia').connect(class_name="SysListView32")
        win_main_Dialog = app.window(best_match='ListBox')
        pane = win_main_Dialog.child_window(best_match=self.filename)
        rect = pane.rectangle()
        cx = int((rect.left+rect.right)/2)
        cy = int((rect.top + rect.bottom)/2)
        mouse.click(button='left', coords=(cx, cy))
        keyboard.send('ctrl+c')
