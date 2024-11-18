def arquivoExiste(nome = str()):
    try:
        teste = open(nome, 'rt')
        teste.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        raise FileExistsError('arquivo não encontrado :(')


def cadastrar(arquivo = str(), valor = str()):
    try:
        a = open(arquivo, 'at')
    except FileNotFoundError:
        raise FileNotFoundError('arquivo inexistente')
    else:
        try:
            a.write(valor + "\n")
        except:
            raise Exception('erro ao gravar no arquivo')
        else:
            a.close()


# "Main"

nomeArquivo = 'bov.txt'

if not arquivoExiste(nomeArquivo):
    criarArquivo(nomeArquivo)

cadastrar(nomeArquivo, 'petr4')
cadastrar(nomeArquivo, 'vale3')
cadastrar(nomeArquivo, 'gbr4')
cadastrar(nomeArquivo, '28.4')
cadastrar(nomeArquivo, '31.3')
cadastrar(nomeArquivo, '15.76')
