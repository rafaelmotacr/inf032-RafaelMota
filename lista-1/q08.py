# 8. supondo um numero 123, imprimi-lo invertido. Exemplo (123, 321). O numero deverá ser armazenado em outra
#variável.

inteiroOriginal = 123
inteiroInvertido = int()

centena = int(inteiroOriginal / 100)
dezena = int(inteiroOriginal % 100 / 10) 
unidade = int(inteiroOriginal % 100 % 10 )
inteiroInvertido = int(unidade * 100 + dezena * 10 + centena)

print('O número invertido é: ' + str(inteiroInvertido))
