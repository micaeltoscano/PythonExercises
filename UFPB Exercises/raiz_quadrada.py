n = int(input("Digite um número: "))
b = 2
p = 0
while True:
    p = (b + n / b) / 2
    if abs(b - p) < 0.0001:
        break
    b = p
   

print(f"A raiz de {n} é aproximadamente: {b:.2f}")