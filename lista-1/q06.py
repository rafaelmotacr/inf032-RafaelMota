# 6. Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?

horas = 3
minutos = 23
segundos = 17
totalSegundos = horas * 60 * 60 + minutos * 60 + segundos

distanciaEmKm = 65
distanciaEmMetros = 65 * 1000

velocidadeMediaMS = distanciaEmMetros / totalSegundos

print('Velocidade média em m/s: ' + str(velocidadeMediaMS))
