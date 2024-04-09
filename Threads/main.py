#Bibliotecas:
import random as rd
import threading
import funcoes

#Criação do vetor:
lista = [rd.randint(0, 1000) for n in range(1000)]

#Visualização das listas criadas:
print("Lista dos números à esquerda: ")
funcoes.lista_esquerda(lista)
print("Lista dos números à direita: ")
funcoes.lista_direita(lista)

#Criação da thread:
thread1 = threading.Thread(target=funcoes.esquerda, args=(lista,))
thread1.start()
thread1.join()

#Exibindo o resultado:
print(f'''O maior valor da esquerda foi {funcoes.esquerda(lista)}
O maior valor da direita foi {funcoes.direita(lista)}''')