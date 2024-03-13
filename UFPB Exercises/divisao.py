dividendo =  int(input("Digite um número a ser o dividendo: "))
divisor =  int(input("Digite um número a ser o divisor: "))
quociente = 0

while (dividendo >= divisor):
    dividendo -= divisor
    quociente += 1
 
print(f" O quociente da divisão é {quociente} e o resto é {dividendo}")



