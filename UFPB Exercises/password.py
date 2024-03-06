#Faça um programa que leia uma senha. Caso o usuário digite a senha errada, a mensagem “Senha incorreta. Digite novamente” deve ser mostrada. Porém, se o usuário digitar a senha errada 3 vezes, a seguinte mensagem deve ser mostrada: “Senha bloqueada.”

senha = input("Digite sua senha: ")
senha_correta = "micael123"
total = 4
tentativa = 1

while (senha != senha_correta and tentativa < 3):
    tentativa = tentativa + 1
    senha = input(f"você errou sua senha. Você tem {total - tentativa} tentativas restantes! Digite novamente: ")
   
        