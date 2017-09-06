from Tabla import *

"""
Funcion para calcular los puntos esperados de acuerdo a la tabla
Recibe el rating del jugador
Y el rating promedio de los jugadores del torneo
"""
def diferencia(ratingJ, ratingP):
    we = ratingJ - ratingP
    return we

def puntosEsperados(ganadas,totales,ratingJ,ratingP):
    we = diferencia(ratingJ,ratingP)
    valorTabla = tablaRating(we)
    puntosTabla = totales * valorTabla
    puntos = ganadas - puntosTabla
    return puntos

def formulaRating(ratingOriginal,constante,resta):
    ratingNuevo = ratingOriginal + (constante * resta)
    return ratingNuevo

def calculaDesempeno(ratingP,ganadas,totales):
    resta = totales - ganadas
    desempeno = ratingP + (400 * (ganadas-resta))/totales
    return desempeno
