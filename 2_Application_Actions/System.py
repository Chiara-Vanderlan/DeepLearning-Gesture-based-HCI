import pyautogui
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode
import time

"""
Function to control system functionalities

Gesture Mapping:
5: Taking a screenshot
3: Switch between applications
4: Increase System Volume
0: Decrease System Volume
2: Activate sleep mode
"""
def control_system(gesture):
    if gesture == None:
        return
    elif gesture == 5:
        print("Taking a screenshot")
        pyautogui.hotkey("winleft", "printscreen")
        time.sleep(1)
    elif gesture == 3:
        print("Switch between applications")
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    elif gesture == 4:
        print("Increase System Volume")
        pyautogui.hotkey('volumeup')
    elif gesture == 0:
        print("Decrease System Volume")
        pyautogui.hotkey('volumedown')
    # elif gesture == 2:
    #     print("Activate sleep mode")
    #     pyautogui.hotkey("winleft", "x")
    #     pyautogui.typewrite("u")
    #     pyautogui.typewrite("s")