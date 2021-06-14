from tkinter import *
from tkinter.ttk import *
import os


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("练习界面")
        self.resizable(0, 0)
        self.geometry("600x320")
        self.setup_UI()

    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="royalblue", width=100)
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="royalblue", width=10, relief=GROOVE)
        # 创建一个Label标签展示图片
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "logingui.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack(padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 识别结果
        self.Label_user = Label(self, text="识别结果:", style="user.TLabel")
        self.Label_user.pack(side=LEFT, padx=10, pady=10)
        self.Entry_user = Entry(self, width=100)
        self.Entry_user.pack(side=LEFT, padx=10, pady=10)


if __name__ == '__main__':
    this_login = MainWindow()
    this_login.mainloop()

# lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
# lbred.pack()
# lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
# lbgreen.pack()
# lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
# lbblue.pack()
# root.mainloop()
