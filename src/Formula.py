from Tabla import *

"""
Funcion para calcular los puntos esperados de acuerdo a la tabla
Recibe el rating del jugador
Y el rating promedio de los jugadores del torneo
"""
def diferencia(ratingJ, ratingP):
    we = ratingJ - ratingP
    return we

"""
Funcion auxiliar para calcular el rating nuevo
Se hace la resta del rating actual con el promedio del rating de los rivales
Ese valor se busca en la tabla de rating
Dicho valor obtenido por la tabla se multiplia por el numero de partidas jugadas
Y se hace la resta del numero de partidas ganadas con el valor obtenido anteriormente
"""
def puntosEsperados(ganadas,totales,ratingJ,ratingP):
    we = diferencia(ratingJ,ratingP)
    valorTabla = tablaRating(we)
    puntosTabla = totales * valorTabla
    puntos = ganadas - puntosTabla
    return puntos

"""
Funcion para obtener el rating nuevo
Se toma el valor obtenido por la funcion puntosEsperados
Se multiplica por la constante y se suma con el rating original
Como resultado obtenemos el rating nuevo
"""
def formulaRating(ratingOriginal,constante,resta):
    ratingNuevo = ((int)(ratingOriginal + (constante * resta)))
    return ratingNuevo

"""
Funcion para calcular el desempenio esperado de un ajedrecista
Se determina a partir de su rating actual, partidas ganads y jugadas
Nos dice el numero de partidos que debe de ganar para mantener dicho rating
"""
def calculaDesempeno(ratingP,ganadas,totales):
    resta = totales - ganadas
    desempeno = ratingP + (400 * (ganadas-resta))/totales
    return desempeno
