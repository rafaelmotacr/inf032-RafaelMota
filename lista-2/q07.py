'''
7. Criar um programa que leia a quantidade de fotas de uma locadora de vídeo possui e o valor que ela cobra
por cada aluguel, mostrando as informações pedidas a seguir: 
a) sabendo que um terço das fitas são
alugadas por mês, exiba o faturamento anual da locadora; 
b)Quando o cliente atrasa a entrega, é cobrada
uma multa de 10% sobre o valor do aluguel. Sabendo que um decimo das fitas alugadas no mês são
devolvidas com atraso, calcule o valor ganho com multas por mês; 
c) sabendo ainda que 2% de fitas se
estragam ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas
que a locadora terá no final do ano.
'''

quantidadeFitas = int(input("> Quantidade de fitas: "))
valorAluguel = int(input("> Valor do aluguel de fitas: "))
umDecimoAluguel = valorAluguel * 0.1

faturamentoAnualAluguel = (valorAluguel * quantidadeFitas / 3) * 12
faturamentoMensalMulta = (umDecimoAluguel + valorAluguel) * quantidadeFitas / 10 
fitasEstragadas = quantidadeFitas * 0.02
fitasDeRposicao = quantidadeFitas * 0.1
totalFinalFitas = quantidadeFitas - fitasEstragadas + fitasDeRposicao

print(f"> Faturamento anual bruto: {faturamentoAnualAluguel}.")
print(f"> Faturamento mensal com multas: {faturamentoMensalMulta}.")
print(f"> Quantidade final de fitas: {totalFinalFitas}.")
