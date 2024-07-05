import pyautogui
from Utils.Focus_on_window import focus_on_window
import time

"""
Function to Control Zoom

Gesture Mapping:
Gesture 0: Raise/Lower Hand
Gesture 3: Leave Meeting
Gesture 4: Mute/Unmute Microphone
Gesture 5: Start/Stop Screen Share
Gesture 7: Start/Stop Video

"""
def dynamic_control_zoom(gesture):
    #Find and activate the movie player window
    window_titles = ["Zoom Meeting"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 20 or gesture == 21:
        pyautogui.hotkey("alt", "v")
        print("Start/Stop Video")
        time.sleep(1)
    elif gesture == 28 or gesture == 29:
        pyautogui.hotkey("alt", "a")
        print("Mute/Unmute Microphone")
        time.sleep(1)
    # elif gesture == 5:
    #     pyautogui.hotkey("alt", "s")
    #     pyautogui.press("enter")
    #     print("Start/Stop Screen Share")
    #     time.sleep(1)
    # elif gesture == 0:
    #     pyautogui.hotkey("alt", "y")
    #     print("Raise/Lower Hand")
    #     time.sleep(1)
    # elif gesture == 3:
    #     pyautogui.hotkey("alt", "q")
    #     pyautogui.press("enter")
    #     print("Leave Meeting")
