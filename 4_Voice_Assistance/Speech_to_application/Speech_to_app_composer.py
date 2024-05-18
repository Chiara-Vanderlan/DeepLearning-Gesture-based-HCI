import sys
from Text_to_application_mapper import text_to_application_mapper

sys.path.append('../4_Voice_Assistance')
from Speech_to_text_generator import speech_to_text
from Text_to_speech_generator import text_to_speech

def speech_to_app_composer():
    text = speech_to_text()
    if text == None:
        text_to_speech("I unabled to hear what you said. Please try again!")
    else:
        text_to_application_mapper(text)
        return
