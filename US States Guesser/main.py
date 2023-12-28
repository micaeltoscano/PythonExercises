import turtle
import pandas

screen= turtle.Screen() #gera a tela
screen.title("U.S guesser game") 

#adiciono a imagem no meu framework
imagem= "blank_states_img.gif"
screen.addshape(imagem)
turtle.shape(imagem)

#crio a tartaruga
tartaruga= turtle.Turtle()
tartaruga.hideturtle()
tartaruga.penup()

#analiso a lista de estados
data= pandas.read_csv("50_states.csv")
estados= data["state"].to_list()

num= 0
respondidas= []
faltaram= []

while num < 50:
    
    resposta= screen.textinput(title= "{}/50".format(num), prompt= "Tente um nome")
    resposta = resposta.title()

    if resposta in estados and resposta not in respondidas:

        coordernada_x= data[data.state == resposta]
        x= int(coordernada_x.x)

        coordernada_y= data[data.state == resposta]
        y= int(coordernada_y.y)

        tartaruga.goto(x,y)
        tartaruga.write(resposta, align="center", font=("Arial", 10, "normal"))
        respondidas.append(resposta)
        num += 1


    elif resposta == "Sair":
       for falta in estados:
           if falta not in respondidas:
               faltaram.append(falta)
               
       data_dict= {
    "Países que faltaram": faltaram
}       
       dataa= pandas.DataFrame(data_dict)
       dataa.to_csv("Relatório de erros")

       break
        
    
screen.exitonclick()
