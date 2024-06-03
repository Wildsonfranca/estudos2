#estudos para aprender python
#Métodos 5Qs
#1º Q :Quais são os dados de entrada  necessarios?
# são numeros 
#2º Q :O que devo fazer com estes dados?
#Devo calcular o fatorial do numero informado pelo usuario
#3º Q :Quais são as restrições deste problema?
#O numero deve ser valor positivo e inteiro
#4º Q :Qual é o resultado esperado?
#o fatorial do numero informado
#5º Q :Qual é asequência de passoas a ser feitas para chegar
# ao resultado esperado?

#projeto 1 
# fatorial de um numero
#crie um programa que receba um numero e imprime seu fatorial.
#inporta a fatorial no python
#from math import factorial
#n = int(input('Digite um numero para calcular seu fatorial:'))
#f = factorial(n)
#print('O fatorial de {} é {}.'.format(n,f))
#modo tradicional
#numero = int(input('informe um numero para saber o seu fatorial:'))
# if numero > 0:
#     fatorial =1
#     for item in range(1,numero +1):
#         fatorial = fatorial * item
#     print(fatorial)    
#     
#projeto 2 
#chuta numero
#escreva um programa que ao iniciar gere um valor aleatorio de 1 a 10
#e permita que o usuario chute um numero até que o valor aleatorio gerado
#no inicio do programa seja chutadi corretamente
#importa biblioteca aleatorio
import random

valor_aleatorio = random.randint(1,10)
#chute = int(input('Chute um numero de 1 a 10 .\n'))
acertou = False
while acertou == False:
    chute = int(input('Chute um numero de 1 a 10 .\n'))
    if chute > valor_aleatorio:
        print('Chute maior que numero aelatorio!')
    elif chute < valor_aleatorio:
        print('Chute menor que numero aleatorio!')
    elif chute == valor_aleatorio:
        acertou == True
        print('Parabéns você acertou!')   
   





