from tkinter import *
from tkinter.ttk import *


class practiseWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("练习界面")
        self.resizable(0, 0)
        self.geometry("800x400")
        self.setup_UI()

    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("top.TPanedwindow", background="white")
        self.Style01.configure("bottom.TPanedwindow", background="white")
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="royalblue")
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", relief=SUNKEN)

        # 创建一个Label标签展示图片
        self.Login_image = PhotoImage(file="./yucun.gif")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack()

        # 上边：输入区域,创建一个容器
        self.Pane_top = PanedWindow(style="top.TPanedwindow")
        self.Pane_top.place(x=4, y=210)

        # 下边：按钮单选区域,创建一个容器
        self.Pane_bottom = PanedWindow(style="bottom.TPanedwindow")
        self.Pane_bottom.place(x=4, y=260)

        # 创建一个Label标签 + Entry   --- 识别结果
        self.Label_user = Label(self.Pane_top, text="识别结果:", style="user.TLabel")
        self.Label_user.pack(side=LEFT)
        self.Entry_user = Entry(self.Pane_top, width=200)
        self.Entry_user.pack(side=LEFT)

        # 暂停
        self.Button_login = Button(self.Pane_bottom, text="暂停", style="TButton")
        self.Button_login.pack(side=LEFT)
        # 生成报告
        self.Button_login = Button(self.Pane_bottom, text="生成报告", style="TButton")
        self.Button_login.pack(side=LEFT)
        # 历史轮毂查询
        self.Button_login = Button(self.Pane_bottom, text="历史轮毂查询", style="TButton")
        self.Button_login.pack(side=LEFT)
        # 设置
        self.Button_login = Button(self.Pane_bottom, text="设置", style="TButton")
        self.Button_login.pack(side=LEFT)
        # 选择区域
        self.Button_login = Button(self.Pane_bottom, text="选择区域", style="TButton")
        self.Button_login.pack(side=LEFT)

        # 返回变量variable=var通常应预先声明变量的类型var=IntVar()或var=StringVar()
        CheckVar1 = IntVar()
        self.Select_cont = Checkbutton(self.Pane_bottom, text='自动标定', variable=CheckVar1)
        self.Select_cont.pack(side=LEFT)


if __name__ == '__main__':
    this_login = practiseWindow()
    this_login.mainloop()
