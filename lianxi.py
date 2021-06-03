from tkinter import *
from tkinter.ttk import *
class interfaceWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('轮毂区域设置')
        self.resizable(0,0)
        self.geometry("1400x800")
        self["bg"]="DarkGray"
        
        # 加载gui
        self.setup_UI()
    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("left.TPanedwindow",background = "navy")
        self.Style01.configure("right.TPanedwindow",background = "skyblue")
        self.Style01.configure("user.TLabel",font = ("华文黑体",20,"bold"),foreground = "royalblue")
        # self.Style01.configure("TEntry",font = ("华文黑体",20,"bold"))
        # self.Style01.configure("TButton",relief=SUNKEN)

        # 左侧顶部添加输出
        self.Pane_left_top = PanedWindow(width = 500,height = 30,style = "left.TPanedwindow")
        self.Pane_left_top.place(x = 4,y = 9)
        
        # 左侧：创建一个容器添加图片
        self.Pane_left_img = PanedWindow(width = 500,height = 540,style = "left.TPanedwindow")
        self.Pane_left_img.place(x = 4,y = 40)

        # 添加图片
        self.Login_image = PhotoImage(file = "./yucun2.gif")
        self.Label_image = Label(self.Pane_left_img,image = self.Login_image)
        self.Label_image.pack()

        # 添加文字
        lb = Label(self.Pane_left_top,text='我是第一个标签',width=36,style="user.TLabel")
        lb.pack()

        # 左侧右部添加按钮
        self.Pane_left_right = PanedWindow(width = 40,height = 540,style = "left.TPanedwindow")
        self.Pane_left_right.place(x = 508,y = 40)

        # 右侧：创建一个容器
        self.Pane_right = PanedWindow(width=700, height=650,style = "right.TPanedwindow")
        self.Pane_right.place(x = 650,y = 40)
     
if __name__ == '__main__':
    this_login = interfaceWindow()
    this_login.mainloop()
