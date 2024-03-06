turno = input("Digite o turno ('M' para matutino, 'V' para vespertino e 'N' para noturno): ")

if turno == "M" or turno == "m":
    print("Bom dia!")
elif turno == "V" or turno == "v":
    print("Boa tarde!")
elif turno == "N" or turno == "n":
    print("Boa noite!")
else:
    print("Opção inválida, tente novamente!")