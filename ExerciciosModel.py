def exercicio01():
    A = 10
    B = 20
    msg = "Antes da Troca: A = {}, B = {}".format(A,B)
    aux = A
    A   = B
    B   = aux
    msg = msg + "\nDepois da Troca: A = {}, B = {}".format(A,B)
    return msg

def exercicio02(A):
    return A - 1

def exercicio03(base, altura):
    if base <= 0:
        return 'Por favor, digite um numero positivo!'
    elif altura <= 0:
        return 'Por favor, digite um numero positivo!'
    else:
        return base * altura

def exercicio04(anos,meses,dias):
    if anos < 0:
        return 'Digite a porra do numero valido caralho'
    elif meses < 0:
        return 'Digite a porra do numero valido caralho'
    elif dias <0:
        return 'Digite a porra do numero valido caralho'
    print('Conversor de Idade em Dias')
    return anos*365 + meses * 30 + dias

def exercicio05():
    print('Insira um numero total de eleitores:')
    totaleleitores = int(input())

    print('Insira um numero total de votos brancos:')
    brancos = int(input())
    msg = 'Porcentagem de votos brancos é: {}'.format(brancos/totaleleitores * 100)

    print('Insira um numero total de votos nulos:')
    nulos = int(input())
    msg = msg + '\nPorcentagem de votos nulos é: {}'.format(nulos/totaleleitores * 100)

    print('Insira um numero total de votos validos:')
    validos = int(input())
    msg = msg + '\nPorcentagem de votos validos é: {}'.format(validos/totaleleitores * 100)
    if brancos + nulos + validos != totaleleitores:
        return 'O numero de total de votos é diferente da porra do total desses eleitores caralho'

    return msg

def exercicio06():
    print ('Insira o seu salario mensal:')
    salario = int(input())

    print('Insira a porcentagem de aumento do seu salário:')
    porcen = int(input())

    return 'Seu novo salario é: {}'.format(salario + (salario*porcen)/100)

def exercicio07():
    print ('Insira o valor do Skyline do Bryan')
    valor = int(input())

    return 'Custo final do consumidor é de: {}'.format(valor + ((valor*28)/100) + ((valor*45)/100))

def exercicio08():
    print ('Insira a primeira nota:')
    A = int(input())

    print('Insira a segunda nota:')
    B = int(input())

    print('Insira a terceira nota:')
    C = int(input())

    return 'Média Final: {}'.format((A+B+C)/3)

def exercicio09():
    print('Insira um numero de maças que deseja comprar:')
    maca = int(input())

    if maca < 12:
        return 'valor da venda é: {}'.format(maca * 1.30)
    else:
        return 'valor da vende é: {}'.format(maca * 1.00)

def exercicio10():
    vet = []
    for i in range(10):
        print('Insira um valor:')
        vet.append(int(input()))

