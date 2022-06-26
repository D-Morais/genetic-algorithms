from random import randint


# Função Objetiva, onde é realizado o calculo da expressão f(x,y).
# o método append() adiciona um elemento a lista
def funcao_objetivo(resultado, valor_x, valor_y):
    valor_da_equacao = 2 - ((valor_x - 2) ** 2) - ((valor_y - 3) ** 2)
    resultado.append(valor_da_equacao)
    if valor_da_equacao == 2:
        return 1
    else:
        return 0


# Printa a tabela formatada
def mostra_tabela(individuos):
    print("=======================================")
    print("|  x  |  y  |  Cromossomo  |  f(x,y)  |")
    print("=======================================")
    for individuo in individuos:
        print(f"|  {individuo[0]}  |  {individuo[1]}  |    {individuo[2]}    |   {individuo[3]} ")
    print("=======================================")


# Caso desejar utilizar números iniciais pré-definidos, utilizamos esse método.
def define_valores(eixo, valores):
    for valor in valores:
        eixo.append(valor)


# Caso desejar utilizar números iniciais aleatórios, utilizamos esse método.
def sorteia_valores(eixo):
    cont = 0
    while (cont < populacao):
        cont = cont + 1
        eixo.append(randint(0, 7))


# Método responsavel por gerar o cromossomo.
# o método zfill() acrescenta zeros a esquerda até completar o número passado por parametro na função.
def gera_cromossomo(cromossomo, valor_x, valor_y):
    cromossomo.append(bin(valor_x)[2:].zfill(3)+bin(valor_y)[2:].zfill(3))


def gera_individuo(individuo, lista):
    individuo.append(lista)


def operador_de_selecao(individuos):
    lista_ordenada = list(sorted(individuos, key=lambda resul: resul[3], reverse=True))
    return lista_ordenada


def ponto_de_corte(individuos):
    quatro_individuos = [individuos[0], individuos[1], individuos[2], individuos[3]]
    return quatro_individuos


def roleta_viciada(individuos):
    num_corte = 4
    nova_lista = []
    aux = []
    cromos = []

    for individuo in individuos:
        aux.append(individuo)
    for genes in aux:
        cromos.append(genes[2])

    cont = 1
    nova_lista.append(cromos[0])
    while(cont < 4):
        aux2 = cromos[0]
        aux2 = aux2[:num_corte]
        aux2 = crossover(aux2)
        nova_lista.append(aux2)
        cont = cont + 1

    cont = 1
    nova_lista.append(cromos[1])
    while(cont < 3):
        aux2 = cromos[1]
        aux2 = aux2[:num_corte]
        aux2 = crossover(aux2)
        nova_lista.append(aux2)
        cont = cont + 1

    cont = 1
    nova_lista.append(cromos[2])
    while (cont < 2):
        aux2 = cromos[2]
        aux2 = aux2[:num_corte]
        aux2 = crossover(aux2)
        nova_lista.append(aux2)
        cont = cont + 1

    nova_lista.append(cromos[3])
    return nova_lista


def crossover(cromo):
    primeiro_genes = str(randint(0, 1))
    segundo_genes = str(randint(0, 1))
    return cromo + primeiro_genes + segundo_genes


def mutacao(cromossomos):
    linha = []
    while True:
        num = randint(0, 9)
        if num not in linha:
            linha.append(num)
            if len(linha) == 5:
                break

    for item in linha:
        individual = cromossomos[item]
        num = randint(0, 5)
        genes_pre = individual[0:num]
        genes_pos = individual[num + 1:len(individual)]
        alterar_genes = individual[num]
        if alterar_genes == "0":
            alterar_genes = "1"
        else:
            alterar_genes = "0"
        individual = genes_pre + alterar_genes + genes_pos
        cromossomos[item] = individual


def separa_genes(cromossomo, genes_x, genes_y):
    for genes in cromossomo:
        genes_x.append(genes[0:3])
        genes_y.append(genes[3:6])


def descodifica(genes):
    if genes == "000":
        return 0
    elif genes == "001":
        return 1
    elif genes == "010":
        return 2
    elif genes == "011":
        return 3
    elif genes == "100":
        return 4
    elif genes == "101":
        return 5
    elif genes == "110":
        return 6
    elif genes == "111":
        return 7


geracoes = 0
populacao = 10
cont = 0
cromossomo = []
X = []
Y = []
individuos = []
resultado = []
novo_individuo = []
op = 0
# Caso utilize valores pré-definidos para executar o AG
valores_iniciais_x = [3, 6, 3, 7, 3, 1, 1, 5, 6, 4]
valores_iniciais_y = [6, 4, 5, 0, 7, 6, 2, 4, 1, 2]

# Caso utilize valores aleatórios para executar o AG
"""
sorteia_valores(x)
sorteia_valores(y)
"""

define_valores(X, valores_iniciais_x)
define_valores(Y, valores_iniciais_y)

while(cont < populacao):
    gera_cromossomo(cromossomo, X[cont], Y[cont])
    op = funcao_objetivo(resultado, X[cont], Y[cont])
    lista = [X[cont], Y[cont], cromossomo[cont], resultado[cont]]
    gera_individuo(individuos, lista)
    cont += 1

mostra_tabela(individuos)

while(op != 1):
    geracoes += 1
    print("")
    print("Geração = ", geracoes)
    print("")
    individuos = operador_de_selecao(individuos)
    mostra_tabela(individuos)
    individuo = ponto_de_corte(individuos)
    cromossomos = roleta_viciada(individuo)
    mutacao(cromossomos)
    X = []
    novo_x = []
    Y = []
    novo_y = []
    separa_genes(cromossomos, X, Y)
    for i in X:
        valor = descodifica(i)
        novo_x.append(valor)
    for j in Y:
        valor = descodifica(j)
        novo_y.append(valor)

    cont = 0
    resultado = []
    nova_lista = []
    novo_individuo = []
    while(cont < 10):
        op = funcao_objetivo(resultado, novo_x[cont], novo_y[cont])
        nova_lista = [novo_x[cont], novo_y[cont], cromossomos[cont], resultado[cont]]
        novo_individuo.append(nova_lista)
        if op == 1:
            print(f"O Algoritmo Genético encontrou a solução depois de {geracoes} gerações!")
            novo_individuo = operador_de_selecao(novo_individuo)
            mostra_tabela(novo_individuo)
            break
        cont += 1
    individuos = novo_individuo

