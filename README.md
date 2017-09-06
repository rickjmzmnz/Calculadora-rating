Calculadora de Rating para determinar la fuerza de juego de un Ajedrecista

Los calculos son basados a partir de el cálculo del rating (puntuación Elo).

La Federación Internacional de Ajedrez (FIDE) tiene clasificada a sus jugadores con un determinado valor de fuerza, este es el rating.
Dicho valor va desde 1000, que es la fuerza más baja, hasta 3000 que es el más fuerte.

El proposito de este programa es poder determinar el nuevo rating de un jugador despúes de haber participado en un torneo.
Este nuevo valor es determinado a partir de las siguientes variables:

Rp = Rating promedio de los rivales a los que se enfrentó
k = una constante que se determina a partir del rating actual del jugador al que se le calculará el nuevo rating
    Esta constante es definida por la FIDE
W = Puntos que realizó en el torneo
We = Puntos esperados a partir de la tabla

Para determinar We tenemos una tabla descrita por Elo, que muestra la probabilidad de un jugador de ganar una partida

A partir de esto podemos determinar al nuevo rating del jugador como:

Rn = Rp + k(W - We)

El programa también determina el desempeño de un jugador como:

D = (Rp + 400 * (triunfos - derrotas))/total de partidas

Este desempeño es un estimado, sí el jugador tiene esta fuerza entonces tendía que tener el valor de triunfos del total de partidas jugadas para conservar su rating