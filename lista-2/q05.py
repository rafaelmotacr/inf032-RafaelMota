# 5. Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km
# com 1 litro. Deverão. Ser fornecidos 
# a) tempo gasto na viagem; 
# b) e a velocidade media. Apresentar os
# valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.

tempoViagem = int(input("> Qual foi o tempo de viagem: "))
velocidadeMedia = float(input("> Qual a velocidade Média: "))
distanciaPercorrida = tempoViagem * velocidadeMedia
print(f"> VELOCIDADE MEDIA: {velocidadeMedia}.")
print(f"> TEMPO GASTO: {tempoViagem}.")
print(f"> DISTÂNCIA PERCORRIDA: {distanciaPercorrida}.")
print(f"> LITROS GASTOS: {distanciaPercorrida / 12:.2f}.")
