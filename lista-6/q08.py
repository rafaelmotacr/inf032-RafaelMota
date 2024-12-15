# 8.Chico tem 1.50m e cresce 2 centímetros por ano, enquanto Juca tem 1.10m e cresce 3 cm por ano. 
# construir um programa que calcule e imprima quantos anos serão necessários para Juca seja maior que Chico;

chicoHeight = 1.50
jucaHeight = 1.10

chicoGrowthRate = 0.02
jucaGrowthRate = 0.03

yearsPassed = 0

while not jucaHeight > chicoHeight:

    jucaHeight += jucaGrowthRate
    chicoHeight += chicoGrowthRate

    yearsPassed = yearsPassed + 1

print(f"> It takes {yearsPassed} years for Juca to surpass Chico. At that moment, Juca will have {jucaHeight:.2f} meters!")
