import cv2 as c
import mediapipe as m
import hand_recognition as hr
import player as p

# Estableciendo configuraciones para utilizar mediapipe. Esta libreria presenta los protocolos para reconocer las manos con la camara.
d = m.solutions.drawing_utils
s = m.solutions.drawing_styles
h = m.solutions.hands

# Se abre una pantalla que graba y almacena el contenido.
video = c.VideoCapture(0)

with h.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    # El programa principal pertenece a un bucle infinito, debido a que debe ejecutarse tras cada movimiento que la camara capture. El final del bucle infinito supondria el final del programa en si.
    timer = 0
    while True:

        r, window = video.read()

        # Si no se abre ninguna ventana debido a algun error, finaliza el bucle.
        if not r or window is None:
            break

        result = hr.recognition(hands, window, d, s, h)

        # Se gira la pantalla para que sea una precisa imagen. Ya que la camara frontal muestra por defecto la imagen invertida.
        window = c.flip(window,1)

        # Se imprime la ventana (la cadena de texto representa el titulo) y empieza a funcionar.
        c.imshow("Piedra, papel o tijera", window)

        # Si se cumplen 5 segundos, se verifica la figura que se eligio.
        if timer > 50:
            try:
                user = p.user(result[0])
                bot = p.cpu()
                
                print("\nElegiste: " + user)    
                print("El bot eligio: " + bot)

                if (p.winner(user, bot)):
                    print("\nTu ganas!\n")

                elif (p.winner(user, bot) is None):
                    print("\nEmpate!\n")

                else:
                    print("\nHas perdido :(\n")

            except TypeError:
                print("No jugaste, el bot gana!")

            break

        # Cada 100 frames, se agrega un segundo al reloj.
        timer = (timer + 1) % 100

        # Si presionamos x en el teclado, finaliza el bucle.
        if c.waitKey(1) & 0xFF == ord("x"):
            break
    
    # Al finalizar el bucle, se destruye la ventana de video creada.
    video.release()
    c.destroyAllWindows()