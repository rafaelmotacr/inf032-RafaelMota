"""
4) Faça um programa que recebe uma string do usuário e informa se ela é um palíndromo.
Um palíndromo é uma frase que, excluindo os espaços em branco, pode ser lida
indiferentemente da esquerda para a direita e da direita para a esquerda. Alguns
palíndromos conhecidos são: ovo, radar, a grama é amarga, a base to teto desaba.
"""

palavra = input("> Digite a palavra que gostaria de saber se é um palíndromo: ").replace(" ", "")
ehPalindromo = palavra == palavra[::-1]
print(f"Eh palindromo? {ehPalindromo}.")
