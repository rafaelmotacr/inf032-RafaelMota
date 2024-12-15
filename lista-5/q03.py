# 3.Entrar com a sigla do estado de uma pessoa, e imprimir se é carioca, Paulista,
# mineira ou outros estados.

acronym = input("> Enter the acronym of the states: ").upper().strip()
answer = acronym == "RJ" or acronym == "SP" or acronym == "MG"
print(f"> Is the friend from São Paulo, Rio de Janeiro or Minas Gerais? Answer: {answer}.")
