def calculo(a,b, lista_cpf):
    #A função calculo recebe 3 parâmetros, "a" que limita quais números vão ser criados, "b" que determina até qual dígito do CPF será realizado o cálculo e "lista_cpf" que é o CPF sem ". e -"
    numeros = [numero for numero in range(a,1,-1)]
    soma = 0
    for n in range(0,b):
        soma += int(lista_cpf[n]) * numeros[n]
    
    calc = soma*10 % 11
    if calc == 10:
        calc = 0
    return calc

def verificacao_digitos_iguais(cpf, lista_cpf):  #Verificar se todos os números do CPF são iguais, ex: "111.111.111-11"
    #Para isso, o programa pega o primeiro dígito e compara com os demais no for. Caso seja igual, ele soma +1
    soma = 0
    for n in range(len(lista_cpf)):
        if lista_cpf[0] == lista_cpf[n]:
            soma += 1
    #Caso a soma seja igual 11, significa que todos os dígitos são iguais, então o CPF não é válido.      
    if soma == 11:
        return False
        
    return True

def main():
    cpf = input("Digite o seu CPF (xxx.xxx.xxx-xx): ")
    #Retira os pontos e o traço do cpf.
    lista_cpf = []
    for m in cpf:
        if m != "." and m != "-":
            lista_cpf.append(m)
    #Se o resto da divisão do cálculo de peso de todos os números antes do "-" for igual ao primeiro dígito após o "-"
    if calculo(10, 9, lista_cpf) == int(cpf[12]):
        #Se o resto da divisão do cálculo de peso de todos os números antes do último digito for igual ao último dígito
        if calculo(11, 10, lista_cpf) == int(cpf[13]):
            #Se todos os dígitos não forem iguais
            if verificacao_digitos_iguais(cpf, lista_cpf):
                print("É válido! ")
            else:
                print("Não é válido! ")

if (__name__ == "__main__"):
    main()
