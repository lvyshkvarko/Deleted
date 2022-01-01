import pyautogui

pyautogui.moveTo(912, 50, 0,5)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a', 'del')
pyautogui.typewrite('google.com')
pyautogui.press('enter')
