from download import Downloading
from selectaddress import SelectAddress
import keyboard

tecentDocApp = "C:\Program Files\TencentDocs\TencentDocs.exe"  # 腾讯文档路径
doc_name = " "  # 文件名称
doc = Downloading(tecentDocApp, doc_name)
doc.tecentdocs()
doc.copy_docs()
wechat_name = " "  # 接收方微信名称
address = SelectAddress(wechat_name)
address.weixin()
print(1)
keyboard.send('ctrl+v')
keyboard.send('enter')
