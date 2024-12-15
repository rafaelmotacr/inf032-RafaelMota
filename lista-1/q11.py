'''11. Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e
compraram alguns itens:
• 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
• 2 pacotes de macarrão: R$ 8,73 cada
• 1 pacote de Molho de tomate: R$ 3,45
• 420g Cebola: R$ 5,40/kg
• 250g de Alho: R$ 30/kg
• 450g de pães franceses: R$ 25/kg
Calcule quanto ficou para cada um.
'''

totalCerveja = 75 * 2.20
totalMacarrao = 2 * 8.73
totalTomate = 3.45
totalCebola = 0.42 * 5.40
totalAlho = 0.25 * 30
totalPao = 0.450 * 25

totalGeral = totalCerveja + totalMacarrao + totalTomate +totalCebola + totalAlho + totalPao
totalIndividual = totalGeral / 4

print('Cada um dos integrantes pagará: R$ ' + str(totalIndividual) + '.')
