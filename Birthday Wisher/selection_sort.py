# -*- coding: utf-8 -*-

from random import randint

def selection_sort(v):
    tamanho = len(v)
    for i in range(tamanho):
        vmin = v[i]
        posmin = i
        j = i + 1
        while(j < tamanho):
            if(v[j] < vmin):
                vmin = v[j]
                posmin = j
            j = j + 1
        
        v[i], v[posmin] = v[posmin], v[i]
        
        
tamanho = 1000

v = [randint(0,tamanho) for i in range(tamanho)]
print(v)
    
print(v)
selection_sort(v)
print()
print(v)

