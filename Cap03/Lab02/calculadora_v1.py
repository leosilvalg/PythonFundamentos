# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************** Python Calculator ********************")


print('Selecione a operação desejada: \n')

def soma(x, y):
    print("Soma: ", x + y)

def sub(x, y):
    print('Subtração: ', x - y)

def mult(x, y):
    print('Multiplicação: ', x * y)

def div(x, y):
    print('Divisão: ', x / y)


print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão \n')

info = input('Digite a operação desejada (1/2/3/4): \n')
    
if int(info) == 1:
    num1 = input('Digite o primeiro valor \n')
    num2 = input('Digite o segundo valor \n')

    soma(int(num1), int(num2))

elif int(info) == 2:
    num1 = input('Digite o primeiro valor \n')
    num2 = input('Digite o segundo valor \n')

    sub(int(num1), int(num2))

elif int(info) == 3:
    num1 = input('Digite o primeiro valor \n')
    num2 = input('Digite o segundo valor \n')

    mult(int(num1), int(num2))

elif int(info) == 4:
    num1 = input('Digite o primeiro valor \n')
    num2 = input('Digite o segundo valor \n')

    div(int(num1), int(num2))

else:
    print('Operação inválida!')