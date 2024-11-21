import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ler o arquivo Excel usando a biblioteca openpyxl
try:
    df = pd.read_excel('Untitled 1.xls', sheet_name='Plan1', engine='openpyxl')
except FileNotFoundError:
    print("O arquivo 'Untitled 1.xls' não foi encontrado. Verifique o nome e o caminho.")
    exit()

# Garantir que as colunas 'A' e 'B' sejam lidas corretamente como float
try:
    vale3 = df['A'].astype(float).values
    ggbr4 = df['B'].astype(float).values
except KeyError:
    print("Certifique-se de que o arquivo possui colunas 'A' e 'B'.")
    exit()

# Calcular os retornos diários
retorno_vale = (vale3[1:] - vale3[:-1]) / vale3[:-1]
retorno_ggbr = (ggbr4[1:] - ggbr4[:-1]) / ggbr4[:-1]

# Criar a figura com 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico do preço da Vale na parte superior
axs[0, 0].plot(vale3, label='Preço Vale3', color='blue')
axs[0, 0].set_title('Preço da Vale (VALE3)')
axs[0, 0].set_xlabel('Dia')
axs[0, 0].set_ylabel('Preço')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Gráfico do retorno da Vale na parte superior
axs[0, 1].plot(retorno_vale, label='Retorno Vale3', color='blue')
axs[0, 1].set_title('Retorno da Vale (VALE3)')
axs[0, 1].set_xlabel('Dia')
axs[0, 1].set_ylabel('Retorno')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Gráfico do preço da Gerdau na parte inferior
axs[1, 0].plot(ggbr4, label='Preço GGBR4', color='red')
axs[1, 0].set_title('Preço da Gerdau (GGBR4)')
axs[1, 0].set_xlabel('Dia')
axs[1, 0].set_ylabel('Preço')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Gráfico do retorno da Gerdau na parte inferior
axs[1, 1].plot(retorno_ggbr, label='Retorno GGBR4', color='red')
axs[1, 1].set_title('Retorno da Gerdau (GGBR4)')
axs[1, 1].set_xlabel('Dia')
axs[1, 1].set_ylabel('Retorno')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Ajustar o layout e mostrar os gráficos
plt.tight_layout()
plt.show()
