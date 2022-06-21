import this
import ExerciciosModel
this.opcao = -1
this.A = 0
this.base = 0
this.altura = 0

def Menu():
    print('Menu\n'          +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n4. Exercício 04' +
          '\n5. Exercício 05' +
          '\n6. Exercício 06' +
          '\n7. Exercício 07' +
          '\n8. Exercício 08' +
          '\n9. Exercício 09' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n0. Sair'         +
          '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def coletarA():
    print('Informe um numero')
    this.A = float(input()) #Convertendo um texto em número com vírgula

def coletarBase():
    print('Informe a base do retângulo')
    this.base = float(input()) #Convertendo um texto em número com vírgula

def coletarAltura():
    print('Informe a altura do retângulo')
    this.altura = float(input())  # Convertendo um texto em número com vírgula

def coletarAnos():
    print('Informe quantos anos você tem:')
    this.anos = float(input())

def coletarMeses():
    print('Informe quanos meses você tem:')
    this.meses = float(input())

def coletarDias():
    print('Informe quantos dias você tem:')
    this.dias = float(input())

def coletarTotalEleitores():
    print('Insira o numero total de Eleitores:')
    this.totaleleitores = float(input())

def coletarBrancos():
    print('Insira o numero total de votos brancos:')
    this.brancos = float(input())

def coletarNulos():
    print('Insira o numero total de votos nulos:')
    this.nulos = float(input())

def coletarValidos():
    print('Insira um numero total de votos validos:')
    this.validos = float(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())
        elif this.opcao == 2:
            coletarA()
            print('O antecessor do {} é: {}'.format(this.A,(ExerciciosModel.exercicio02(this.A))))
        elif this.opcao == 3:
            coletarAltura()
            coletarBase()
            print('A área do retângulo multiplicando a base de {} e a altura de {} é: {}'
                  .format(this.base, this.altura,(ExerciciosModel.exercicio03(this.base, this.altura))))
        elif this.opcao == 4:
            coletarAnos()
            coletarMeses()
            coletarDias()
            print('O total de dias da sua idade é: {}'.format((ExerciciosModel.exercicio04(this.anos, this.meses, this.dias))))
        elif this.opcao == 5:
            print(ExerciciosModel.exercicio05())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio06())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio07())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio08())
        elif this.opcao == 9:
            print(ExerciciosModel.exercicio09())
        elif this.opcao == 10:
            print(ExerciciosModel.exercicio10())
        elif this.opcao == 11:
            print(ExerciciosModel.exercicio11())
        elif this.opcao == 12:
            print(ExerciciosModel.exercicio12())
        elif this.opcao == 13:
            print(ExerciciosModel.exercicio13())
        elif this.opcao == 14:
            print(ExerciciosModel.exercicio14())
        elif this.opcao == 15:
            print(ExerciciosModel.exercicio15())
        elif this.opcao == 16:
            print(ExerciciosModel.exercicio16())
        elif this.opcao == 17:
            print(ExerciciosModel.exercicio17())
        elif this.opcao == 18:
            print(ExerciciosModel.exercicio18())
        elif this.opcao == 19:
            print(ExerciciosModel.exercicio19())
        elif this.opcao == 20:
            print(ExerciciosModel.exercicio20())
        else:
            print('Opção informada não é valida!')







