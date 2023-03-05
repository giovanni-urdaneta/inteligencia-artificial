import cv2 as c
import mediapipe as m

# Detecta, en conjunto, la forma que 
def recognition(hands, window, drawing, styles, player_hand):

    # Se traduce contenido capturado en la ventana a un espacio de colores conocidos por el ser humano, tambien denominado: espacio de colores RGB.
    window = c.cvtColor(window, c.COLOR_BGR2RGB)

    # En esta variable se almacenara lo que la camara capture con respecto a nuestras manos. Los patrones para definir una determinada figura. 
    results = hands.process(window)

    # Se produce el proceso inverso en cuanto al espacio de colores y la variable vuelve a su estado anterior.
    window = c.cvtColor(window, c.COLOR_RGB2BGR)
        
    # Se rastrean los movimientos de las manos a traves de puntos de referencia.
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Se dibujan estos puntos de referencia.
            drawing.draw_landmarks(window, landmarks, player_hand.HAND_CONNECTIONS, styles.get_default_hand_landmarks_style(), styles.get_default_hand_connections_style())

    # Contiene los puntos de referencia capturados en las manos reconocidas.
    return results.multi_hand_landmarks