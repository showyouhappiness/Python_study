import pyautogui


def testCenterAndSingleClick():
    # 获取当前屏幕的分辨率
    screenWidth, screenHeight = pyautogui.size()
    print(screenWidth, screenHeight)

    # 获取当前鼠标的位置
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)
    # 在获取的鼠标位置双击一下
    pyautogui.click(419, 440, button='left', duration=0.25, clicks=2)

    # 等待三秒
    pyautogui.sleep(3)
    # 使用键盘按键并输入账号test
    pyautogui.typewrite('a123', interval=0.25)
    # 按下tab键
    pyautogui.press('tab')
    # 使用键盘按键并输入密码crf123a123
    pyautogui.typewrite('123456', interval=0.25)
    # 按下tab键
    pyautogui.press('tab')
    # 输入验证码
    pyautogui.typewrite('1234', interval=0.25)

    # 按下数字键旁边的回车键
    pyautogui.press('enter')
    # 单击
    pyautogui.click(1155, 649, button='left', duration=0.25, clicks=1)

    pyautogui.sleep(10)
    # 关闭软件
    pyautogui.hotkey('alt', 'f4')

