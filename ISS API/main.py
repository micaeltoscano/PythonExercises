import requests
import datetime 
import smtplib
import time

minha_lat= 0 #sualat
minha_long= 0 #sualong

parametros= {

    "lat": minha_lat,
    "lng": minha_long,
    "formatted": 0,
}

def e_noite():
    request= requests.get("https://api.sunrise-sunset.org/json", params= parametros)
    request.raise_for_status()

    sunset = int(request.json()["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(request.json()["results"]["sunrise"].split("T")[1].split(":")[0])

    horario= datetime.datetime.now().hour

    if horario >= sunset or horario <= sunrise:
        return True

def esta_em_cima():
    iss = requests.get("http://api.open-notify.org/iss-now.json")

    dados_iss_latitude= float(iss.json()["iss_position"]["latitude"])
    dados_iss_longitude= float(iss.json()["iss_position"]["longitude"])

    print(dados_iss_latitude, dados_iss_longitude)

    if dados_iss_latitude >= minha_lat-5 and dados_iss_latitude <= minha_lat+5:
        if dados_iss_longitude >= minha_long-5 and dados_iss_longitude <= minha_long+5:
            return True
        
def enviar_email():
    meu_email= "seuemailaqui"
    senha= "suasenhaqui"

    with smtplib.SMTP("smtp.gmail.com") as conexao:
        conexao.starttls()
        conexao.login(meu_email, senha)
        conexao.sendmail(from_addr=meu_email, to_addrs="@gmail.com", msg= "OLHE PARA CIMA, TEM UM SATELITE EM CIMA DE TU UAUUUUUUUU")
        
while True:
    time.sleep(60)
    if e_noite() and esta_em_cima():
        enviar_email()

        
    
    



