def formatar_data(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    lista = data.split("/")

    if (int(lista[1]) > 12):
        print("Não existe um mês correspondente ao informado! ")
    else:
        #Sobre o mês: transformo o mês da lista em inteiro e procuro seu index na lista meses, diminuindo 1 para que o mês seja o correspondente. 
        print(f"Sua data formatada é: {lista[0]} de {meses[int(lista[1]) - 1]} de {lista[2]}")
        
def main():
    data = input("Digite sua data de nascimento no formato (dd/mm/aaaa): ")
    formatar_data(data)

if (__name__ == "__main__"):
    main()