from time import time

class Sort():
    def BubbleSort(self, lista):
        n = len(lista)
        i = 0
        for i in range(1, n):
            for j in range(n - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def insertionsort(self, lista):
        for index in range(1,len(lista)):
            valor= lista[index]
            i= index -1
            while i >= 0:
                if valor < lista[i]:
                    lista[i + 1] = lista[i]

                    lista[i] = valor
                    i = i -1
                else:
                    break
        return lista

