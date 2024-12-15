# 3. Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber
# quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

aulasNoMes = 2 * 4
mesesDeAuala = 4
minimoDepPresenca =  (mesesDeAuala * aulasNoMes) * 0.25
print('Olá, Davinir! Você ainda pode faltar ' + str(minimoDepPresenca) + ' aulas este semestre!')
