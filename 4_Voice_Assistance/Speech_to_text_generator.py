import speech_recognition as sr

def speech_to_text(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text 
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
        return None