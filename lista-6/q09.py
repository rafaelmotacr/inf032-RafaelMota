"""
9.Uma empresa defornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. para cada consumidor, são digitados os seguintes dados:
a)Numero do consumidor; 
b)Quantidade de kWh consumidos durante o mês; 
c)tipo do consumidor -> 1-residencial, preço em reias de kWh = 0,3 / 2-comercial, 
preço em reias de kWh = 0,5 / 3-industrial, preço em reias de kWh = 0,7. Os dados 
devem ser lidos ate que seja encontrado um consumidor com numero 0(zero). 
calcular e imprimir: 
a) o custo total para cada consumidor; 
b) o total de consumo para os 3(três) tipos de consumidor; 
c) a media de consumo dos tipos 1 e 2.
"""

consumerNumber = int()
kwhMonth = int()
consumerType = str()

while True:
    consumerNumber = int(input("> Number of Consumer: "))
    kwhMonth = int (input("> Number oh kwh Consumed: "))
    consumerType  = input("> Type of Consumer: ")
    if consumerNumber == 0:
        break
    print("====================================")
    print(f"> Total for consumer {consumerNumber}: {} ")
