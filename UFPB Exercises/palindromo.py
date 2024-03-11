def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    soma = palavra + palavra
    comprimento = len(soma)
    esquerda = 0
    direita = comprimento - 1

    while esquerda < direita:
        print(soma[esquerda])
        if (soma[esquerda] != soma[direita]):
            return False
        esquerda += 1
        direita -= 1
    return True

palavra = "A base do teto desaba"

if palindromo(palavra):
    print("É palídromo!")
else:
    print("Não é palíndromo!")