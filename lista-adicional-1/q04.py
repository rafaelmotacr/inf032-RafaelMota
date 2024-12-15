'''4. Criar a lista com nomes das bolsas de valores do mundo: Bolsas = [‘dow’, ‘ibov’, ‘ftse’,
‘dax’, ‘nasdaq’, ‘cac’]. Fatiá-la conforme os itens a seguir.
(a) Selecionar as três primeiras.
(b) Incluir a sublista Bs = [‘hong kong’, ‘merval’] na lista anterior.
(c) Descobrir qual o índice da ‘nasdaq’.
(d) Remover ‘cac’ da lista.
(e) Inserir “sp&500” como índice 2 na lista de bolsas, mas sem excluir nenhum
elemento já inscrito.'''

bolsas = ['dow', 'ibov', 'ftse', 'dax','nasdaq', 'cac']
subListaDaMinhaTristeza = ['hong kong', 'merval',]

print(f"A) {bolsas[0:3]}.")
bolsas.append(subListaDaMinhaTristeza)
print(f"B) {bolsas}.")
print(f"C) {bolsas.index('nasdaq')}.")
bolsas.remove('cac')
print(f"D) {bolsas}.")
bolsas.insert(2, 'sp&500')
print(f"E) {bolsas}.")