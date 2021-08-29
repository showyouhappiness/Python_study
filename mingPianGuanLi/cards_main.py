#!C:\Users\l1477\AppData\Local\Programs\Python\Python38\python.exe
import cards_tools

# 无限循环,由用户主动决定什么时候退出循环
while True:
    # 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 对输入的结果进行判断
    # 如果是1,2,3,则是针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_card()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()
    # 如果是0,则退出系统
    elif action_str == "0":
        print("欢迎下次使用【名片管理系统】")
        break
    # 如果是其他的,则提示输入错误
    else:
        print("输入错误,请重新输入!")
