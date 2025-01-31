"""
2) Na usina de Angra dos Reis, os técnicos analisam a perda de massa de um material
radioativo. Sabendo-se que este perde 25% de sua massa a cada 30 segundos, criar um
programa que imprima o tempo necessário para que a massa deste material se torne
menor que 0,10 gramas. O programa pode calcular o tempo para várias massas.
"""

tempoEmSegundos = 0
while True:
    tmp = qtdMassa = float(input("> Digite a massa do material [999 para sair]: "))
    if qtdMassa == 999:
        break
    while tmp > 0.10:
        decaimento = tmp * 0.25
        tmp -= decaimento
        tempoEmSegundos += 30
    print(f"> Para que a massa de {qtdMassa} seja menor que 0.10 gramas, serão necessários: ")
    print(f"{tempoEmSegundos} segundos.")      
    print(f"{tempoEmSegundos / 60:.0f} minutos.")
    print(f"{tempoEmSegundos / 60 / 60:.0f} horas.")
