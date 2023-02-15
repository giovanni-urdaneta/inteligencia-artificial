# Giovanni Urdaneta - 28288477

# debe instalarse la libreria pyaudio para que el programa funcione
from voice_settings import setVoice, speak
from text_to_speech import listen
import pywhatkit as p


# definiendo voz de alexa
voice = setVoice()


def main():
    print('Debes decir mi nombre para empezar...')
    greeting = listen("es-VE", 3)
    
    # si alexa entiende la oracion
    if greeting:
        # la cadena resultante se convierte en minuscula para generalizar los resultados
        greeting = greeting.lower()

        if 'alexa' in greeting:
            speak(voice, "Dime, en que puedo ayudarte?")
            print('Escuchando...')
            output = listen("es-VE", 5)

            if output: 
                output = output.lower()

                if 'adios' in output or 'adiós' in output:
                    speak(voice, "Adios")

                elif 'busca en' in output:
                    if 'google' in output:
                        speak(voice, "Que necesitas que busque?")
                        # obteniendo busqueda...
                        print("Escuchando...")
                        search = listen('es-VE', 7)

                        p.search(search)

                    elif 'youtube' in output: 
                        speak(voice, "Que video quieres que ponga?")
                        # obteniendo busqueda...
                        print("Escuchando...")
                        search = listen('es-VE', 7)

                        p.playonyt(search)
                        
                    else:
                        speak(voice, "No conozco la plataforma que acabas de mencionar")

            else:
                speak(voice, "No entendi nada")

        else:
            speak(voice, "No entendi nada")
            
    else:
        speak(voice, "Si no dices mi nombre, no puedo ayudarte")


main()