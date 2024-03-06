primeiro_lado = float(input("Digite o tamanho do primeiro lado do triângulo: "))
segundo_lado = float(input("Digite o tamanho do segundo lado do triângulo: "))
terceiro_lado = float(input("Digite o tamanho do terceiro lado do triângulo: "))

if primeiro_lado == segundo_lado and primeiro_lado == terceiro_lado:
    print("É um triângulo equilátero!")
elif primeiro_lado == segundo_lado and primeiro_lado != terceiro_lado:
    print("É um triângulo isósceles!")
else:
    print("É um triângulo escaleno!")