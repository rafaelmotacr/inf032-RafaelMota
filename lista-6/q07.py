#7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3% ao ano, e um pais B com 7.000.000 de 
# habitantes e uma taxa de natalidade de 2% ao ano. calcular e imprimir o tempo necessário para que a população do pais A ultrapasse a população do pais B;

countryABithRate = 0.03
countryBBithRate = 0.02

countryAPopulation = 5000000
countryBPopulation = 7000000

yearsPassed = 0

while not countryAPopulation > countryBPopulation:

    countryAPopulation = countryAPopulation + (countryAPopulation * countryABithRate) 
    countryBPopulation = countryBPopulation + (countryBPopulation * countryBBithRate)

    yearsPassed = yearsPassed + 1

print(f"> It takes {yearsPassed} years for population A to surpass  population B.")
