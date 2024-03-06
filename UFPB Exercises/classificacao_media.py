primeira_nota = float(input("Digite a sua primeira nota: "))
segunda_nota = float(input("Digite a sua segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media <= 10:
    if media >= 9:
        print(f"Sua média foi: {media}, portanto você foi conceito A!")
    elif media >= 7.5:
        print(f"Sua média foi: {media}, portanto você foi conceito B!")
    elif media >= 6:
        print(f"Sua média foi: {media}, portanto você foi conceito C!")
    elif media >= 4:
        print(f"Sua média foi: {media}, portanto você foi conceito D!")
    else:
        print(f"Sua média foi: {media}, portanto você foi conceito E!")
else:
    print("Digite notas válidas, lembrando-se que o máximo que se pode tirar na prova é 10!")