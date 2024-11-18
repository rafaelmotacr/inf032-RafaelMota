'''Os dados a seguir representam os preços diários de fechamentos no pregão da
Bovespa entre os meses de setembro e outubro de 2019. A coluna A do Excel se
refere a VALE3 (Vale do Rio Doce) e a coluna B indica GGBR4 (Gerdau). Os dados
estão em um arquivo Excel na planilha denominada Plan1.

Deseja-se, então, que esses dados sejam importados para o Python com a biblioteca
xlrd e que se responda aos itens a seguir.
(a) Importar os dados do Excel e transformar a coluna A em uma variável que
represente a Vale e a coluna B em outra variável que represente a coluna B.
(b) Transformar as variáveis em vetores usando a biblioteca numpy.
(c) Fazer os dois gráficos dos preços da Vale e da Gerdau usando subplot. Colocar
a Vale na parte superior da figura e a Gerdau na parte inferior.
(d) Calcular os retornos das duas empresas e plotar os quatro gráficos (preço da
Vale e seu retorno; preço da Gerdau e seu retorno) no formato de uma matriz
com 2×2 elementos.'''

import pandas as pd

# Ler o arquivo Excel
df = pd.read_excel('Untitled 1.xls', sheet_name='Sheet1')
# Agora você pode acessar as colunas diretamente como Series ou transformá-las em arrays
vale3 = df['A'].values
ggbr4 = df['B'].values

# Exibir os dados
print(vale3)
print(ggbr4)



