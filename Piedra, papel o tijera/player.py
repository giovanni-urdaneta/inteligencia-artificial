# Segun la posicion de los puntos de referencia, uno con respecto a otro, se determina que forma tomo la mano
import random

# Jugada del usuario, basada en los puntos de referencia obtenidos.
def user(hand):
    l = hand.landmark

    if all(l[i].y < l[i+3].y for i in range(9, 20, 4)):
        return "Piedra" 
    
    elif l[13].y < l[16].y and l[17].y < l[20].y:
        return "Tijera"
    
    else:
        return "Papel"
    
# Devuelve un valor aleatorio entre piedra, papel o tijera (jugada del cpu).
def cpu():
    plays = ["Piedra", "Papel", "Tijera"]
    random.shuffle(plays)
    return plays[0]

# Decide quien de los dos gana.
def winner(user, bot):
    if user == "Piedra":
        if bot == "Papel":
            return False
        
        if bot == "Tijera":
            return True

    if user == "Papel":
        if bot == "Piedra":
            return True
        
        if bot == "Tijera":
            return False
    
    if user == "Tijera":
        if bot == "Piedra":
            return False
        
        if bot == "Papel":
            return True