"""5. Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome,
idade, telefone. O programa deve ler um 5 dados completos, e imprimir todos os itens do
dicionário no formato chave: nome-idade-fone."""

pessoas = [
    {"nome":"Gabriel","idade":23,"numero":"00000001"},
    {"nome":"João","idade":21, "numero":"00000002"},
    {"nome":"Carlos","idade":19, "numero":"00000003"}, 
    {"nome":"Silas","idade":25,"numero":"00000004"},
    {"nome":"Ana Júlia","idade":23,"numero":"00000005"}]

dicionarioPessoas = {
    "000.000.000-01": pessoas[0],
    "000.000.000-02": pessoas[1],
    "000.000.000-03" :pessoas[2],
    "000.000.000-04": pessoas[3],
    "000.000.000-05": pessoas[4]}

print(f"Nome: {dicionarioPessoas.get("000.000.000-01").get("nome")}, idade: {dicionarioPessoas.get("000.000.000-01").get("idade")}, telefone: {dicionarioPessoas.get("000.000.000-01").get("numero")}.")
print(f"Nome: {dicionarioPessoas.get("000.000.000-02").get("nome")}, idade: {dicionarioPessoas.get("000.000.000-02").get("idade")}, telefone: {dicionarioPessoas.get("000.000.000-02").get("numero")}.")
print(f"Nome: {dicionarioPessoas.get("000.000.000-03").get("nome")}, idade: {dicionarioPessoas.get("000.000.000-03").get("idade")}, telefone: {dicionarioPessoas.get("000.000.000-03").get("numero")}.")
print(f"Nome: {dicionarioPessoas.get("000.000.000-04").get("nome")}, idade: {dicionarioPessoas.get("000.000.000-04").get("idade")}, telefone: {dicionarioPessoas.get("000.000.000-04").get("numero")}.")
print(f"Nome: {dicionarioPessoas.get("000.000.000-05").get("nome")}, idade: {dicionarioPessoas.get("000.000.000-05").get("idade")}, telefone: {dicionarioPessoas.get("000.000.000-05").get("numero")}.")
