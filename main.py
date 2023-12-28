import pandas as pd
import datetime as dt
import smtplib
import random 

meu_email= #COLOQUESEUEMAIL
senha= #COOQUESUASENHA

agora= dt.datetime.now()    #uso datetime para pegar o dia, mês e ano
dia_da_semana= agora.day
mes= agora.month
ano= agora.year

data= pd.read_csv("birthdays.csv")                  #abro o arquivo csv para pegar o dia e o mês que estamos
dia_aniversario= data[data.day == dia_da_semana] 
mes_aniversario= data[data.month == mes]

def enviar_email():

    lista_de_cartas= ["letter_1.txt", "letter_2.txt", "letter_3.txt"]  #pego uma carta aleatoria
    aleatoria= random.choice(lista_de_cartas)
    print(aleatoria)

    with open(f"{aleatoria}", "r", encoding="utf-8") as mensagens:   

        conteudo= mensagens.read()  #abro o conteúdo da carta

        for n in range (len(nome)):
            conteudo_modificado= conteudo.replace("[NAME]", nome[n])   #Caso haja mais de um aniversariante no dia, preciso que seja enviado apenas um email por pessoa, por isso o "nome[n]"

            with open("texto_modificado", "w") as mensagem:   #escrevo o nome na carta modificada
                mensagem.write(conteudo_modificado)
        
            with open ("texto_modificado", "r") as novo_arquivo: #faço a máquina ler o arquivo para atribuir uma variável a carta que será enviada
                mensagem_com_nome= novo_arquivo.read()
            
            with smtplib.SMTP("smtp.gmail.com") as conexao: #envio a carta
                conexao.starttls()
                conexao.login(meu_email, senha)
                conexao.sendmail(from_addr= meu_email, to_addrs= email[n],  msg= mensagem_com_nome) #uso o email[n] para enviar apenas 1 email
                
if len(dia_aniversario) >= 1 and len(mes_aniversario) >= 1: #Uso o if para verificar se há alguém aniversariando e, se houver, ele transforma o nome dele e o email em lista
    email= dia_aniversario.email.to_list()
    nome= dia_aniversario.name.to_list()

    enviar_email()
    

