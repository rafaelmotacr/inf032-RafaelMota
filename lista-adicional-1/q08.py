import pandas as pd 
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


excel = pd.read_excel('Dados_vale__Gerdau.xlsx', sheet_name='Plan1', header=None)


excel[0] = pd.to_numeric(excel[0], errors='coerce')
excel[1] = pd.to_numeric(excel[1], errors='coerce')


excel.dropna(inplace=True)


vale = np.array(excel[0])
gerdau = np.array(excel[1])


dias = np.arange(0, len(vale))

plt.subplot(211)
plt.plot(dias, vale)
plt.title('Preços da Vale')

plt.subplot(212)
plt.plot(dias, gerdau)
plt.title('Preços da Gerdau')
plt.show()


ret_vale = (vale[1:] - vale[:-1]) / vale[:-1]
ret_gerdau = (gerdau[1:] - gerdau[:-1]) / gerdau[:-1]


dias_ret = np.arange(0, len(ret_vale))


plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.plot(dias, vale)
plt.title('Preço da Vale')

plt.subplot(222)
plt.plot(dias, gerdau)
plt.title('Preço da Gerdau')

plt.subplot(223)
plt.plot(dias_ret, ret_vale)
plt.title('Retorno da Vale')

plt.subplot(224)
plt.plot(dias_ret, ret_gerdau)
plt.title('Retorno da Gerdau')

plt.tight_layout()  
plt.show()
