
"""
Dada la diferencia entre el rating del jugador y el rating promedio de los rivales
Se da un valor de la tabla de diferencias de rating
"""
def tablaRating(n):
    if (n <= 677 and n > 589 or n > 677):
        return 0.99
    elif (n <= 589 and n > 538):
        return 0.98
    elif (n <= 538 and n > 501):
        return 0.97
    elif (n <= 501 and n > 470):
        return 0.96
    elif (n <= 470 and n > 444):
        return 0.95
    elif (n <= 444 and n > 422):
        return 0.94
    elif (n <= 422 and n > 401):
        return 0.93
    elif (n <= 401 and n > 383):
        return 0.92
    elif (n <= 383 and n > 366):
        return 0.91
    elif (n <= 366 and n > 351):
        return 0.90
    elif (n <= 351 and n > 335):
        return 0.89
    elif (n <= 335 and n > 322):
        return 0.88
    elif (n <= 322 and n > 309):
        return 0.87
    elif (n <= 309 and n > 296):
        return 0.86
    elif (n <= 296 and n > 284):
        return 0.85
    elif (n <= 284 and n > 273):
        return 0.84
    elif (n <= 273 and n > 262):
        return 0.83
    elif (n <= 262 and n > 251):
        return 0.82
    elif (n <= 251 and n > 240):
        return 0.81
    elif (n <= 240 and n > 230):
        return 0.80
    elif (n <= 230 and n > 220):
        return 0.79
    elif (n <= 220 and n > 211):
        return 0.78
    elif (n <= 211 and n > 202):
        return 0.77
    elif (n <= 202 and n > 193):
        return 0.76
    elif (n <= 193 and n > 184):
        return 0.75
    elif (n <= 184 and n > 175):
        return 0.74
    elif (n <= 175 and n > 166):
        return 0.73
    elif (n <= 166 and n > 158):
        return 0.72
    elif (n <= 158 and n > 149):
        return 0.71
    elif (n <= 149 and n > 141):
        return 0.70
    elif (n <= 141 and n > 133):
        return 0.69
    elif (n <= 133 and n > 125):
        return 0.68
    elif (n <= 125 and n > 117):
        return 0.67
    elif (n <= 117 and n > 110):
        return 0.66
    elif (n <= 110 and n > 102):
        return 0.65
    elif (n <= 102 and n > 95):
        return 0.64
    elif (n <= 95 and n > 87):
        return 0.63
    elif (n <= 87 and n > 80):
        return 0.62
    elif (n <= 80 and n > 72):
        return 0.61
    elif (n <= 72 and n > 65):
        return 0.60
    elif (n <= 65 and n > 57):
        return 0.59
    elif (n <= 57 and n > 50):
        return 0.58
    elif (n <= 50 and n > 43):
        return 0.57
    elif (n <= 43 and n > 36):
        return 0.56
    elif (n <= 36 and n > 29):
        return 0.55
    elif (n <= 29 and n > 21):
        return 0.54
    elif (n <= 21 and n > 14):
        return 0.53
    elif (n <= 14 and n > 7):
        return 0.52
    elif (n <= 7 and n > 0):
        return 0.51
    elif (n <= 0 and n > (-7)):
        return 0.50
    elif (n <= (-7) and n > (-14)):
        return 0.49
    elif (n <= (-14) and n > (-21)):
        return 0.48
    elif (n <= (-21) and n > (-29)):
        return 0.47
    elif (n <= (-29) and n > (-36)):
        return 0.46
    elif (n <= (-36) and n > (-43)):
        return 0.45
    elif (n <= (-43) and n > (-50)):
        return 0.44
    elif (n <= (-50) and n > (-57)):
        return 0.43
    elif (n <= (-57) and n > (-65)):
        return 0.42
    elif (n <= (-65) and n > (-72)):
        return 0.41
    elif (n <= (-72) and n > (-80)):
        return 0.40
    elif (n <= (-80) and n > (-87)):
        return 0.39
    elif (n <= (-87) and n > (-95)):
        return 0.38
    elif (n <= (-95) and n > (-102)):
        return 0.37
    elif (n <= (-102) and n > (-110)):
        return 0.36
    elif (n <= (-110) and n > (-117)):
        return 0.35
    elif (n <= (-117) and n > (-125)):
        return 0.34
    elif (n <= (-125) and n > (-133)):
        return 0.33
    elif (n <= (-133) and n > (-141)):
        return 0.32
    elif (n <= (-141) and n > (-149)):
        return 0.31
    elif (n <= (-149) and n > (-158)):
        return 0.30
    elif (n <= (-158) and n > (-166)):
        return 0.29
    elif (n <= (-166) and n > (-175)):
        return 0.28
    elif (n <= (-175) and n > (-184)):
        return 0.27
    elif (n <= (-184) and n > (-193)):
        return 0.26
    elif (n <= (-193) and n > (-202)):
        return 0.25
    elif (n <= (-202) and n > (-211)):
        return 0.24
    elif (n <= (-211) and n > (-220)):
        return 0.23
    elif (n <= (-220) and n > (-230)):
        return 0.22
    elif (n <= (-230) and n > (-240)):
        return 0.21
    elif (n <= (-240) and n > (-251)):
        return 0.20
    elif (n <= (-251) and n > (-262)):
        return 0.19
    elif (n <= (-262) and n > (-273)):
        return 0.18
    elif (n <= (-273) and n > (-284)):
        return 0.17
    elif (n <= (-284) and n > (-296)):
        return 0.16
    elif (n <= (-296) and n > (-309)):
        return 0.15
    elif (n <= (-309) and n > (-322)):
        return 0.14
    elif (n <= (-322) and n > (-335)):
        return 0.13
    elif (n <= (-335) and n > (-351)):
        return 0.12
    elif (n <= (-351) and n > (-366)):
        return 0.11
    elif (n <= (-366) and n > (-383)):
        return 0.10
    elif (n <= (-383) and n > (-401)):
        return 0.09
    elif (n <= (-401) and n > (-422)):
        return 0.08
    elif (n <= (-422) and n > (-444)):
        return 0.07
    elif (n <= (-444) and n > (-470)):
        return 0.06
    elif (n <= (-470) and n > (-501)):
        return 0.05
    elif (n <= (-501) and n > (-538)):
        return 0.04
    elif (n <= (-538) and n > (-589)):
        return 0.03
    elif (n <= (-589) and n > (-676)):
        return 0.02
    elif (n <= (-677)):
        return 0.01
