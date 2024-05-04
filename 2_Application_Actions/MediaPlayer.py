import pyautogui
import time
from FocusOnWindow import focus_on_window

"""
Function to control media player

Gesture Mapping:
Gesture 0: Play/Stop the movie
Gesture 4: Volume Increased
Gesture 2: Volume Decreased
Gesture 3: Switch to full-screen mode
"""
def control_media_player(gesture):
    #Find and activae the movie player window
    window_titles = ["Movies", "VLC media player"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 0:
        pyautogui.press("space")
        print("Play/Stop the movie")
    elif gesture == 4:
        pyautogui.scroll(1)
        print("Volume Increased")
    elif gesture == 2:
        pyautogui.scroll(-1)
        print("Volume Decreased")
    elif gesture == 3:
        pyautogui.press("f")
        print("Switch to full-screen mode")
