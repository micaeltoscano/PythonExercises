#Bibliotecas:
import random as rd
import threading
import funcoes

#Criação do vetor:
lista = [rd.randint(0, 1000) for n in range(1000)]

#Visualização das listas criadas:

#Criação da thread:
thread1 = threading.Thread(target=funcoes.segunda_metade, args=(lista,)).start()
thread2 = threading.Thread(target=funcoes.terceira_metade, args=(lista,)).start()
thread3 = threading.Thread(target=funcoes.quarta_metade, args=(lista,)).start()

thread1.join()
thread2.join()
thread3.join()

