#Método de ordenação Bolha e Inserção
import random

def criaVetor(n):
      vetor = [0]*n
      for i in range(n):
            vetor[i] = random.randint(0,100)
      return vetor

def bolha(vetor):
      for k in range(len(vetor)):
            for i in range(len(vetor)-1-k):
                  if vetor[i] > vetor[i + 1]:
                        temp = vetor[i]
                        vetor[i] = vetor[i + 1]
                        vetor[i + 1] = temp
      return vetor

def insercao(vetor):
      for k in range(1, len(vetor)):
            x = vetor[k]
            i = k
            while i>0 and x<vetor[i - 1]:
                  vetor[i] = vetor[i - 1]
                  i -= 1
            vetor[i] = x
      return vetor

def main():
      n = 5
      vetor = criaVetor(n)
      print('Vetor =',vetor)
      print('Vetor ordenado =',bolha(vetor))
      print('Vetor ordenado por inserção =',insercao(vetor))

main()

input()
