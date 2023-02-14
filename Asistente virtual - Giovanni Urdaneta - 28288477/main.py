# Giovanni Urdaneta - 28288477

# debe instalarse la libreria pyaudio para que el programa funcione
from voice_settings import setVoice, speak
from text_to_speech import listen
import pywhatkit as p

# definiendo voz de alexa
voice = setVoice()

def main():
    print('Escuchando...')
    output = listen("es-VE", 5)
    
    # si alexa entiende la oracion
    if output:
        # la cadena resultante se convierte en minuscula para generalizar los resultados
        output = output.lower()
        if 'alexa' in output:
            if 'busca en' in output:
                if 'google' in output:
                    speak(voice, "Que necesitas que busque?")
                    # obteniendo busqueda...
                    print("Escuchando")
                    search = listen('es-VE', 7)
                    p.search(search)

                elif 'youtube' in output: 
                    speak(voice, "Que video quieres que ponga?")
                    # obteniendo busqueda...
                    print("Escuchando")
                    search = listen('es-VE', 7)
                    p.playonyt(search)
                    
                else:
                    speak(voice, "No conozco la plataforma que acabas de mencionar. Por favor, intentalo de nuevo")
                    main()
            
    else:
        speak(voice, "No entendi nada. Por favor, intentalo de nuevo")
        main()

main()