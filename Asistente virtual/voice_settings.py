# Giovanni Urdaneta - 28288477

# la voz utilizada ha sido instalada en las configuraciones de windows
import pyttsx3

# determinando voz de alexa
def setVoice():
    v = pyttsx3.init()
    voices = v.getProperty('voices')
    v.setProperty('voice', voices[2].id) # voz latina femenina
    v.setProperty('rate', 150) # velocidad de la voz
    return v

def speak(v, text):
    v.say(text)
    v.runAndWait()