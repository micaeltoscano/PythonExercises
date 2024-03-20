# -*- coding: utf-8 -*-

from random import randint

# def linear_search(v, ele):
#     for i in range(len(v)):
#         if(v[i] == ele):
#             return i
#         if(v[i] > ele):
#             break
#     return -1  


tamanho = 100

v = [randint(0,tamanho) for i in range(tamanho)]
print(v)

# v.sort()
# print(v)


# pos = linear_search(v, 11)
# if(pos >= 0):
#     print("Achei na posição:" + str(pos))
# else:
#     print("O elemento não está no vetor!")

