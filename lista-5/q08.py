# 8. entrar com o nome, nota 1 e nota 2 de um aluno, imprimir nome, Nota1, nota2, média e a mensagem
# aprovado, reprovado ou em prova final. (a média é 7 para aprovado, 3 para reprovado, e as demais para
# prova final.

grades = list()
studentName = input("> Enter Your Name: ")

grades.append(int(input("> First Grade: ")))
grades.append(int(input("> Second Grade: ")))
grades.append(int(input("> Third Grade: ")))

average = (grades[0] + grades[1] + grades[2]) / 3

print("> ", end = "")
if average >= 7:
    print("Approved", end = "")
elif average >= 3:
    print("Failed", end = "")
else:
    print("Final test", end = "")
print(f" with averagage media: {average}")