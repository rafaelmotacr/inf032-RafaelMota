"""
3) Faça um programa que calcule o menor número possível de notas (cédulas) que um
valor, inserido pelo usuário, pode ser decomposto. As notas consideradas são de 100,
50, 20, 10, 5, 2 e 1.
"""

notasDeCem = notasDeCinquenta = notasDeVinte = notasDeDez = notasDecinco = notasDeDois = notasDeUm = 0

while True:
    valorCopia = valorOriginal = float(input("> Digite o valor que deseja receber em cédulas: "))    
    if valorOriginal <= 0:
        print("> ERRO: O valor digitado precisa ser positivo e maior que zero!")
        continue
    break

if valorCopia >= 100:
    notasDeCem = valorCopia // 100
    valorCopia %= 100

if valorCopia >= 50:
    notasDeCinquenta = valorCopia // 50
    valorCopia %= 50

if valorCopia >= 20:
    notasDeVinte = valorCopia // 20
    valorCopia %= 20
    
if valorCopia >= 10:
    notasDeDez = valorCopia // 10
    valorCopia %= 10

if valorCopia >= 5:
    notasDecinco = valorCopia // 5
    valorCopia %= 5

if valorCopia >= 2:
    notasDeDois = valorCopia // 2
    valorCopia %= 2   
    
if valorCopia >= 1:
    notasDeUm = valorCopia // 1
    valorCopia %= 1

print(f"> Para o valor {valorOriginal}, você irá precisar de: ")
if notasDeCem > 0:
    print(f"{notasDeCem:.0f} nota(s) de cem reais.")
if notasDeCinquenta > 0:
    print(f"{notasDeCinquenta:.0f} nota(s) de cinquenta reais.")
if notasDeVinte > 0:
    print(f"{notasDeVinte:.0f} nota(s) de vinte reais.")
if notasDeDez > 0:
    print(f"{notasDeDez:.0f} nota(s) de dez reais.")
if notasDecinco > 0:
    print(f"{notasDecinco:.0f} nota(s) de cinco reais.")
if notasDeDois > 0:
    print(f"{notasDeDois:.0f} nota(s) de dois reais.")    
if notasDeUm > 0:
    print(f"{notasDeUm:.0f} 5.")    
    
