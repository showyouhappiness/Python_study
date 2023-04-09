import pyautogui

# 获取当前屏幕的分辨率
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)


# 获取当前鼠标的位置
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
# 在获取的鼠标位置双击一下
pyautogui.click(267, 331, button='left', duration=0.25, clicks=2)

# 等待三秒
pyautogui.sleep(3)
# 使用键盘按键并输入密码123456
pyautogui.typewrite('123456', interval=0.25)

# 按下回车键
pyautogui.press('enter')
