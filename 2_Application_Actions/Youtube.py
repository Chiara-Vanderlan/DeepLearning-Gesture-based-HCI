import pyautogui
import time
import webbrowser
import sys

from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode

sys.path.append('../4_Voice_Assistance')
from Speech_to_text_generator import speech_to_text

# Variable to track if YouTube has been opened before
youtube_opened = False

"""
Function to control reading and browsing functionalities

Gesture Mapping:
4: Scrolling down
0: Scrolling up
3: Zooming in
2: Zooming out
"""
def control_youtube(gesture):
    global youtube_opened
    if not youtube_opened:
        webbrowser.open("https://www.youtube.com")
        youtube_opened = True

    #Find and activae the YouTube-Google Chrome window
    window_titles = ["YouTube - Google Chrome"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 4:
        print("Scrolling down")
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif gesture == 0:
        print("Scrolling up")
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    elif gesture == 3:
        print("Search Youtube")
        time.sleep(2)
        pyautogui.click(x=800, y=190)
        text = speech_to_text()

        while text is None:
            text = speech_to_text()
            if text is None:
                print("Speech recognition failed. Trying again...")

        print("Typing '{}' into the search bar".format(text))
        pyautogui.typewrite(text, interval=0.1)
        pyautogui.press('enter')
        time.sleep(2)
    elif gesture == 2:
        print("Play video")
        pyautogui.click(x=800, y=600)
        time.sleep(3)
    elif gesture == 5:
        print("Activate full-screen mode")
        pyautogui.press('f')




