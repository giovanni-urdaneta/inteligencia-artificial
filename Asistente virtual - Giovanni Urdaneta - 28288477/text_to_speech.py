# Giovanni Urdaneta - 28288477

import speech_recognition as s

# el input tiene por defecto un tiempo de escucha de 3 segundos
def listen(l, time = 3):
    recognizer = s.Recognizer()

    with s.Microphone() as microphone:
        input = recognizer.listen(microphone, phrase_time_limit=time)

    try:
        return recognizer.recognize_google(input, language=l)

    except:
        return None 