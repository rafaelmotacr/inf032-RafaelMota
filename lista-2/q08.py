"""
8. Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, o qual é calculado da
seguinte maneira. Exemplo: numero conta 235, somar o numero da conta com seu inverso : 235+532=767.
Multiplicar cada digito pela sua ordem posicional e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. O
ultimo digito desse resultado é o digito verificador da conta (40-> 0 )
"""

numeroConta = input("> Digite o número da conta: ")
inverSoNumeroConta = numeroConta[::-1]
soma = str(int(numeroConta) + int(inverSoNumeroConta)) 
digitoVerificador = int(soma[0]) * 1 + int(soma[1]) * 2 + int(soma[2]) * 3
print(f"> Digito verificador: {digitoVerificador}.")
