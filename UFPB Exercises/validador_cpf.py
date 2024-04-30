def primeira_verificacao(cpf, lista_cpf):

    numeros = [numero for numero in range(10,1,-1)]
    soma = 0
    for n in range(0,9):
        soma += int(lista_cpf[n]) * numeros[n]
    
    calc = soma*10 % 11
    if calc == 10:
        calc = 0
    if calc == int(cpf[12]):
        return True
    
    return False

def segunda_verificacao(cpf, lista_cpf):
    if primeira_verificacao(cpf,lista_cpf):

        numeros = [numero for numero in range(11,1,-1)]
        soma = 0
        for n in range(0,10):
            soma += int(lista_cpf[n]) * numeros[n]
        
        calc = soma*10 % 11
        if calc == 10:
            calc = 0
        if calc == int(cpf[13]):
            return True
        
    return False

def terceira_verificacao(cpf, lista_cpf):
    if segunda_verificacao(cpf, lista_cpf):

        soma = 0
        for n in range(len(lista_cpf)):
            if lista_cpf[0] == lista_cpf[n]:
                soma += 1
                
        if soma == 11:
            return False
        
    return True

def main():
    cpf = input("Digite o seu CPF: ")

    lista_cpf = []
    for m in cpf:
        if m != "." and m != "-":
            lista_cpf.append(m)

    if terceira_verificacao(cpf, lista_cpf):
        print("É valido! ")
    else:
        print("Não é valido! ")

if (__name__ == "__main__"):
    main()


    