#Bibliotecas:
import random as rd
import threading
import funcoes

#Criação do vetor de 1 milhão de números:
lista = [rd.randint(0, 999999) for n in range(1000000)]

#Visualização das listas criadas:
print(lista)
funcoes.exibicao_lista(funcoes.primeiro, funcoes.segunda_metade, funcoes.terceira_metade, funcoes.quarta_metade, lista)

#Criação da thread:
thread1 = threading.Thread(target=funcoes.segunda_metade, args=(lista,))
thread2 = threading.Thread(target=funcoes.terceira_metade, args=(lista,))
thread3 = threading.Thread(target=funcoes.quarta_metade, args=(lista,))

#Inicialização:
funcoes.inicializacao(thread1,thread2,thread3)

#Exibição dos resultados:
print(f'''O maior número da primeira metade: {max(funcoes.primeiro(lista))} 
O maior número da segunda metade: {max(funcoes.segunda_metade(lista))}  
O maior número da terceira metade: {max(funcoes.terceira_metade(lista))} 
O maior número da quarta metade: {max(funcoes.quarta_metade(lista))} ''')


