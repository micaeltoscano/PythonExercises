from tkinter import *
from tkinter import messagebox
import pandas
import csv
import random

def cadastro_roupa():
    def accccionado():
        noome= nome.get()
        codigoo= codigo.get()
        valoor= valor.get()
        tamanhoo= tamanho.get()
        quantidadee= quantidade.get()

        quantidade_real= int(quantidadee) - 1
        
        if len(noome) == 0 or len(codigoo) == 0 or len(valoor) == 0 or len(tamanhoo) == 0 or len(quantidadee) == 0:
            messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
        else:
            try:
                valoor = int(valoor)
                quantidadee = int(quantidadee)
                arquivo_csv = "Pasta1.csv"
                with open(arquivo_csv, mode='a', newline='') as arquivo:
                    escritor_csv = csv.writer(arquivo)
                    escritor_csv.writerow([noome,codigoo,valoor,tamanhoo,quantidade_real])

            except ValueError:
                messagebox.showerror(title="Erro", message="Você não digitou valores válidos para valor ou quantidade (certifique-se de que sejam números, não letras).")


    def deletar_nome():
        nome.delete(0, END)

    def deletar_valor():
        valor.delete(0, END)
        
    def deletar_tamanho():
        tamanho.delete(0, END)
        
    def deletar_quantidade():
        quantidade.delete(0, END)


    janela_cadastro = Tk()
    janela_cadastro.minsize(500,500)

    mensagem_nome= Label(janela_cadastro, text= "Nome da roupa: ")
    mensagem_nome.grid(column=0, row=4)
    nome= Entry(janela_cadastro)
    nome.grid(column=1, row=4)
    botao_delete_nome= Button(janela_cadastro, text= "Limpar", command= deletar_nome)
    botao_delete_nome.grid(column=2,row=4)
    
    mensagem_codigo= Label(janela_cadastro, text= "Código da roupa: ")
    mensagem_codigo.grid(column=0, row=1)
    codigo= Entry(janela_cadastro)
    codigo.grid(column=1, row=1)
    codigo.insert(0, "a")

    mensagem_valor= Label(janela_cadastro, text= "Valor da roupa: ")
    mensagem_valor.grid(column=0, row=2)
    valor= Entry(janela_cadastro)
    valor.grid(column=1, row=2)
    botao_delete_valor= Button(janela_cadastro, text= "Limpar", command= deletar_valor)
    botao_delete_valor.grid(column=2,row=2)

    mensagem_tamanho= Label(janela_cadastro, text= "Tamanho da roupa: ")
    mensagem_tamanho.grid(column=0, row=3)
    tamanho= Entry(janela_cadastro)
    tamanho.grid(column=1, row=3)
    botao_delete_tamanho= Button(janela_cadastro, text= "Limpar", command= deletar_tamanho)
    botao_delete_tamanho.grid(column=2,row=3)

    mensagem_quantidade= Label(janela_cadastro, text= "Quantidade da roupa: ")
    mensagem_quantidade.grid(column=0, row=5)
    quantidade= Entry(janela_cadastro)
    quantidade.grid(column=1, row=5)
    botao_delete_quantidade= Button(janela_cadastro, text= "Limpar", command= deletar_quantidade)
    botao_delete_quantidade.grid(column=2,row=5)

    botao_procurooo= Button(janela_cadastro, text= "Adicionar", command= accccionado)
    botao_procurooo.grid(column=1, row=6)

def cadastro_venda():

    def accionado():
        codigo_a_remover = input_coodigo.get()
        codigo_do_cliente_a_cadastrar= input_codigo.get()
        dataaa = pandas.read_csv("Pasta1.csv")

        if len(codigo_a_remover) == 0 or len(codigo_do_cliente_a_cadastrar) == 0:
            messagebox.showerror(title= "Erro", message= "Você precisa preencher o código do cliente e o código do produto para prosseguir!")
        else:
            print(dataaa)
            dataaa.loc[dataaa['Codigo'] == codigo_a_remover, 'quantidade'] -= 1
            dataaa = dataaa[dataaa['quantidade'] != -1]
            dataaa.to_csv("Pasta1.csv", index=False)
            
            peca= dataaa.loc[dataaa['Codigo'] == codigo_a_remover, 'Nome'].to_list()
            for a in peca:
                nome_peca = a

            valorpeca= dataaa.loc[dataaa['Codigo'] == codigo_a_remover, 'valor'].to_list()
            for b in valorpeca:
                valor_peca = b

            tamanhopeca= dataaa.loc[dataaa['Codigo'] == codigo_a_remover, 'tamanho'].to_list()
            for c in tamanhopeca:
                tamanho_peca = c

            procurar_nome_cliente= pandas.read_csv("clientes.csv")
            namee= procurar_nome_cliente.loc[procurar_nome_cliente["codigo_cliente"] == codigo_do_cliente_a_cadastrar, "nome"].to_list()
            for u in namee:
                name = u

            arquivo= "vendas.csv"
            try:
                with open (arquivo, mode= "a", newline= "" ) as archive:
                    escrever_csv= csv.writer(archive)
                    escrever_csv.writerow([name,nome_peca,valor_peca,tamanho_peca])
            except UnboundLocalError:
                messagebox.showinfo(title="Informações", message="Esse produto acabou de sair de estoque!")

            acrescentar_compra= pandas.read_csv("clientes.csv")
            
            acrescentar_compra.loc[acrescentar_compra["codigo_cliente"] == codigo_do_cliente_a_cadastrar, 'compras'] += 1
            acrescentar_compra.to_csv("clientes.csv", index=False)


    def procurar_codigo_cliente():

        nome_do_cliente= input_conferir_codigo.get()
        try:
            if len(nome_do_cliente) == 0:
                messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
            else:
                arquivo_vendas= pandas.read_csv("clientes.csv")
                localizar_codigo= arquivo_vendas.loc[arquivo_vendas["nome"] == nome_do_cliente, "codigo_cliente"].to_list()
                for n in localizar_codigo:
                    codigo_localizado = n
                preencher_espaço4.insert(0, codigo_localizado)
                
        except UnboundLocalError:
            messagebox.showerror(title="Erro", message="O nome digitado não consta no sistema! Lembre-se de cadastrar o cliente, caso seja a primeira compra dele!")

    def cadastro_cliente():

        def acccionado():
            nome = input_nome.get()
            contato = input_contato.get()
            sexo = input_sexo.get()
            idade= input_idade.get()

            if len(nome) == 0 or len(contato) == 0 or len(sexo) == 0 or len(idade) == 0:
                messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
            else:

                compras = 0
                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                escolha_aleatoria= [random.choice(letters) for _ in range(1,6)]
                random.shuffle(escolha_aleatoria)
                codigo_gerado= "".join(escolha_aleatoria).lower()

                arquivo_csv = "clientes.csv"
                with open(arquivo_csv, mode='a', newline='') as arquivo:
                    escritor_csv = csv.writer(arquivo)
                    escritor_csv.writerow([codigo_gerado,nome,idade,sexo,contato,compras])

        segunda_janela= Tk()
        segunda_janela.minsize(500,500)

        mensagem_nome= Label(segunda_janela, text= "Digite o nome do cliente: ")
        mensagem_nome.grid(column=0, row=1)
        input_nome= Entry(segunda_janela)
        input_nome.grid(column=1, row=1)

        mensagem_contato= Label(segunda_janela, text= "Digite o número do cliente: ")
        mensagem_contato.grid(column=0, row=2)
        input_contato= Entry(segunda_janela)
        input_contato.grid(column=1, row=2)

        mensagem_sexo= Label(segunda_janela, text= "Digite o gênero do(a) filho(a) do cliente: ")
        mensagem_sexo.grid(column=0, row=3)
        input_sexo= Entry(segunda_janela)
        input_sexo.grid(column=1, row=3)

        botao_procurooo= Button(segunda_janela, text= "Adicionar", command= acccionado)
        botao_procurooo.grid(column=1, row=5)

        mensagem_idade= Label(segunda_janela, text= "Digite a idade do(a) filho(a) do(a) cliente: ")
        mensagem_idade.grid(column=0, row=4)
        input_idade= Entry(segunda_janela)
        input_idade.grid(column=1, row=4)


    terceira_janela= Tk()
    terceira_janela.minsize(300,300)

    codigo_do_cliente= Label(terceira_janela, text= "Digite o Código do cliente: ")
    codigo_do_cliente.grid(column=0, row=1)
    input_codigo= Entry(terceira_janela)
    input_codigo.grid(column=1,row=1)

    mensagem_coodigo= Label(terceira_janela, text= "Digite o código do produto: ")
    mensagem_coodigo.grid(column=0, row=2)
    input_coodigo= Entry(terceira_janela)
    input_coodigo.grid(column=1, row=2)
    input_coodigo.insert(0, "a")
        
    botao_procuroo= Button(terceira_janela, text= "Cadastrar venda", command= accionado)
    botao_procuroo.grid(column=1, row=3)

    conferir_codigo= Label(terceira_janela, text= "Digite o nome do cliente para conferir seu código: ")
    conferir_codigo.grid(column=0,row=6)
    input_conferir_codigo= Entry(terceira_janela)
    input_conferir_codigo.grid(column=1,row=6)
    botao_conferir_codigo= Button(terceira_janela, text="Procurar", command=procurar_codigo_cliente)
    botao_conferir_codigo.grid(column=2, row=6)

    pergunta_cadastro_cliente= Label(terceira_janela, text="Primeira compra do cliente? Cadastre:")
    pergunta_cadastro_cliente.grid(column=0,row=9)
    botao_cadastro_cliente= Button(terceira_janela, text="Cadastrar", command= cadastro_cliente)
    botao_cadastro_cliente.grid(column=1,row=9)

    preencher_espaço1= Label(terceira_janela, text="")
    preencher_espaço1.grid(column=0, row=4)
    preencher_espaço2= Label(terceira_janela, text="")
    preencher_espaço2.grid(column=0, row=5)
    preencher_espaço3= Label(terceira_janela, text="")
    preencher_espaço3.grid(column=0, row=10)
    preencher_espaço4= Entry(terceira_janela)
    preencher_espaço4.grid(column=1, row=7)
    preencher_espaço5= Label(terceira_janela, text="")
    preencher_espaço5.grid(column=0, row=8)
  
def procuro_estoque():

    def acionar():
         tamanho_valor= input_tamanho.get()
         tamaho_valor_int= int(tamanho_valor)
         if len(tamanho_valor) == 0:
             messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
         else:
            dadosss= pandas.read_csv("Pasta1.csv")
            taamanho= dadosss[dadosss.tamanho ==  tamaho_valor_int]
            if not taamanho.empty:
                lista_de_nomes= taamanho["Nome"].to_list()
                print(lista_de_nomes)
                messagebox.showinfo(title="Dados", message= f"As roupas de tamanho { tamaho_valor_int} são: {', '.join(map(str, lista_de_nomes))}")
            else:
                messagebox.showerror(title="Dados", message= "Não há peças desse tamanho disponíveis! ")


    def procurar_nome():
         nome_procurar= input_nome.get()
         if len(nome_procurar) == 0:
             messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
         else:
            dadossss= pandas.read_csv("Pasta1.csv")
            print(dadossss)
            nomeee= dadossss[dadossss.Nome == nome_procurar]
            if not nomeee.empty:
                lista_de_valores= nomeee["valor"].to_list()
                lista_de_tamanhos= nomeee["tamanho"].to_list()
                messagebox.showinfo(title="Dados", message= f"O(s) tamanho(s) disponível(eis) da(s) {nome_procurar} é(são): {', '.join(map(str, lista_de_tamanhos))}")
            else:  
                messagebox.showerror(title="Dados", message= "A peça não está disponível ")
         
    quarta_janela= Tk()
    quarta_janela.minsize(500,500)

    mensagem_tamanho= Label(quarta_janela, text= "Digite o tamanho: ")
    mensagem_tamanho.grid(column=0, row=2)

    input_tamanho= Entry(quarta_janela)
    input_tamanho.grid(column=1, row=2)

    botao_tamanho= Button(quarta_janela, text= "Procurar", command= acionar)
    botao_tamanho.grid(column= 2, row=2)

    mensagem_nome= Label(quarta_janela, text= "Digite o nome: ")
    mensagem_nome.grid(column=0, row=3)

    input_nome= Entry(quarta_janela)
    input_nome.grid(column=1, row=3)

    botao_nome= Button(quarta_janela, text= "Procurar", command=procurar_nome)
    botao_nome.grid(column= 2, row=3)

def gerencia():
    janela_gerencia= Tk()
    janela_gerencia.minsize(500,500)

    relatorio_vendas= Label(janela_gerencia,text= 'Relatório de vendas')
    relatorio_vendas.grid(column=0, row=1)
    relatorio_vendas_botao= Button(janela_gerencia,text= "Acessar")
    relatorio_vendas_botao.grid(column=1, row=1)

    acompanhamento_financeiro= Label(janela_gerencia,text= "Acompanhamento Financeiro")
    acompanhamento_financeiro.grid(column=0, row=2)
    acompanhamento_financeiro_botao= Button(janela_gerencia,text= "Acessar")
    acompanhamento_financeiro_botao.grid(column=1, row=2)

    acompanhar_cliente= Label(janela_gerencia,text= "Acompanhar cliente")
    acompanhar_cliente.grid(column=0, row=3)
    acompanhar_cliente_botao= Button(janela_gerencia,text= "Acessar")
    acompanhar_cliente_botao.grid(column=1, row=3)

    estoque= Label(janela_gerencia, text="Verificar estoque")
    estoque.grid(column=0, row=4)
    estoque_botao= Button(janela_gerencia, text= "Acessar")
    estoque_botao.grid(column=1, row=4)

def aba_clientela():
     
     def cadastro_cliente():

        def acccionado():
            nome = input_nome.get()
            contato = input_contato.get()
            sexo = input_sexo.get()
            idade= input_idade.get()

            if len(nome) == 0 or len(contato) == 0 or len(sexo) == 0 or len(idade) == 0:
                messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
            else:

                compras = 0
                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                escolha_aleatoria= [random.choice(letters) for _ in range(1,6)]
                random.shuffle(escolha_aleatoria)
                codigo_gerado= "".join(escolha_aleatoria).lower()

                arquivo_csv = "clientes.csv"
                with open(arquivo_csv, mode='a', newline='') as arquivo:
                    escritor_csv = csv.writer(arquivo)
                    escritor_csv.writerow([codigo_gerado,nome,idade,sexo,contato,compras])

        segunda_janela= Tk()
        segunda_janela.minsize(500,500)

        mensagem_nome= Label(segunda_janela, text= "Digite o nome do cliente: ")
        mensagem_nome.grid(column=0, row=1)
        input_nome= Entry(segunda_janela)
        input_nome.grid(column=1, row=1)

        mensagem_contato= Label(segunda_janela, text= "Digite o número do cliente: ")
        mensagem_contato.grid(column=0, row=2)
        input_contato= Entry(segunda_janela)
        input_contato.grid(column=1, row=2)

        mensagem_sexo= Label(segunda_janela, text= "Digite o gênero do(a) filho(a) do cliente: ")
        mensagem_sexo.grid(column=0, row=3)
        input_sexo= Entry(segunda_janela)
        input_sexo.grid(column=1, row=3)

        botao_procurooo= Button(segunda_janela, text= "Adicionar", command= acccionado)
        botao_procurooo.grid(column=1, row=5)

        mensagem_idade= Label(segunda_janela, text= "Digite a idade do(a) filho(a) do(a) cliente: ")
        mensagem_idade.grid(column=0, row=4)
        input_idade= Entry(segunda_janela)
        input_idade.grid(column=1, row=4)

     def procuro_cliente():
            def procurando():
                nome_cliente= input_cliente.get()
                if len(nome_cliente) == 0:
                    messagebox.showerror(title= "Erro", message= "Você precisa preencher todos os campos para prosseguir!")
                else:
                    try:
                        dados_procuro_cliente= pandas.read_csv("clientes.csv")
                        cliente= dados_procuro_cliente[dados_procuro_cliente.nome == nome_cliente]

                        lista_cliente= cliente.contato.to_list()
                        for n in lista_cliente:
                            contato_cliente = n
                        idd_cliente= cliente.idade.to_list()
                        for a in idd_cliente:
                            idade_cliente= a
                        sxx_cliente= cliente.sexo.to_list()
                        for b in sxx_cliente:
                            sexo_cliente = b
                        cps_cliente= cliente.compras.to_list()
                        for c in cps_cliente:
                            compras_cliente = c
                        messagebox.showinfo(title= "dados do cliente", message= f"os dados de {nome_cliente} são:" f"\n Contato: {contato_cliente}" f"\n Idade do(a) filho(a): {idade_cliente}" f"\n Sexo do filho(a) do(a) cliente: {sexo_cliente}" f"\n Compras do(a) cliente: {compras_cliente}")
                    except UnboundLocalError:
                        messagebox.showerror(title= "Erro", message= "Esse nome não está cadastrado na lista de contatos")
              
            quinta_janela= Tk()
            quinta_janela.minsize(500,500)


            nome_cliente= Label(quinta_janela, text= "Digite o nome do cliente que deseja procurar: ")
            nome_cliente.grid(column= 0, row=1)

            input_cliente= Entry(quinta_janela)
            input_cliente.grid(column=1, row=1)

            botao_cliente= Button(quinta_janela, text="Procurar", command= procurando)
            botao_cliente.grid(column=1, row=2)

     janela_clientela= Tk()
     janela_clientela.minsize(500,500)

     opção1= Label(janela_clientela, text= "Você deseja: ")
     opção1.grid(column=1, row=1)

     botao1= Button(janela_clientela,text= "Cadastrar cliente", command= cadastro_cliente)
     botao1.grid(column=2, row=1)

     botao2= Button(janela_clientela,text= "Procurar cliente", command= procuro_cliente)
     botao2.grid(column=3, row=1)

def instrucoes():
     messagebox.showinfo(title= "Instruções:", message= "1: O código deve sempre começar com a letra a" "\n 2: Nunca cadastre uma venda ou um produto com o excel aberto")

     leitor_teste= pandas.read_csv("Pasta1.csv")
     print(leitor_teste)

janela= Tk()

janela.title("Moda Pingo Infantil")
janela.config(padx=10, pady=10)

canvas= Canvas(width=300, height=300)
logo= PhotoImage(file="logo.png" )
canvas.create_image(150,150, image=logo)
canvas.grid(column= 1,row=0)

cadastrar_roupa= Button(text= "Cadastrar roupa no estoque", command= cadastro_roupa)
cadastrar_roupa.grid(column=1, row=4)

Aba_cliente= Button(text="Aba Cliente", command= aba_clientela)
Aba_cliente.grid(column= 1, row= 1)

cadastrar_venda= Button(text="Cadastrar venda", command=cadastro_venda)
cadastrar_venda.grid(column=1, row=3)

procurar_estoque= Button(text="Procurar roupa no estoque", command= procuro_estoque)
procurar_estoque.grid(column=1, row=5)

instrucao= Button(text="Instruções", command=instrucoes)
instrucao.grid(column=1, row=6)

aba_gerente= Button(text= "Aba Gerente", command= gerencia)
aba_gerente.grid(column=1, row=2)

janela.mainloop()