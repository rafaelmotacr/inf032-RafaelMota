"""
9.Uma empresa defornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. para cada consumidor, são digitados os seguintes dados:
a)Numero do consumidor; 
b)Quantidade de kWh consumidos durante o mês; 
c)tipo do consumidor -> 
    1-residencial, preço em reias de kWh = 0,3 / 
    2-comercial, preço em reias de kWh = 0,5 / 
    3-industrial, preço em reias de kWh = 0,7. Os dados 
devem ser lidos ate que seja encontrado um consumidor com numero 0(zero). 
calcular e imprimir: 
a) o custo total para cada consumidor; 
b) o total de consumo para os 3(três) tipos de consumidor; 
c) a media de consumo dos tipos 1 e 2.
"""
consumersList = list()
residentialConsumption = commercialConsumption = industrialConsumption = 0
commercialConsumptionConsumers = residentialConsumptionConsumers = 0

consumerTax = {
    "1": 0.3,  # Residencial
    "2": 0.5,  # Comercial
    "3": 0.7   # Industrial
}

print("====================================")
while True:
    consumerID = int(input("> Number of Consumer: ").strip())
    if consumerID == 0:
        print("====================================")
        break
    kwhMonth = float(input("> Number oh kwh Consumed: ").strip())
    consumerType  = input("> Type of Consumer [1/2/3]: ").strip()[0]
    consumersList.append({"consumerID": consumerID, 
                        "kwhMonth": kwhMonth,
                        "consumerType":consumerType})
    print("====================================")

for consumer in consumersList:
    consumerTotal = consumer.get("kwhMonth") * consumerTax.get(consumer.get("consumerType")) 
    print(f"> Total cost for consumer: {consumer.get("consumerID")} = {consumerTotal}.")
    match consumer.get("consumerType"):
        case '1':
            residentialConsumption += consumer.get("kwhMonth") 
            residentialConsumptionConsumers += 1
        case '2':
            commercialConsumption += consumer.get("kwhMonth") 
            commercialConsumptionConsumers += 1 
        case '3':
            industrialConsumption += consumer.get("kwhMonth") 
    print("====================================")

print(f"> Total Residential consumption: {residentialConsumption}.")
print(f"> Total Commercial consumption : {commercialConsumption}.")
print(f"> Total Industrial consumption : {industrialConsumption}.")
print("====================================")
print(f"> Average Residentiial consumption: {residentialConsumption / residentialConsumptionConsumers if residentialConsumptionConsumers > 0 else 0.0}.")
print(f"> Average Commercial consumption  : {commercialConsumption / commercialConsumptionConsumers if commercialConsumptionConsumers > 0 else 0.0}.")
print("====================================")
