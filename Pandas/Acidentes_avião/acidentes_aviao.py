import pandas as pd

#ANOTAÇÕES: Como as "keys" do csv não estava definida, tive que determiná-las no names, além de ter informado o padrão de delimitação.
def transformar_em_dict(lista):
    dict = {}

    for n in lista:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n] += 1

    return dict

def incidencia(dicionario):

    maior_inc = max(dicionario, key= lambda x: dicionario[x])
    soma = sum(dicionario.values())

    return maior_inc, soma

def main():
    caminho = "ocorrencia_tipo.csv"
    data = pd.read_csv(caminho, delimiter=';', names=["codigo_ocorrencia1", "ocorrencia_tipo", "ocorrencia_tipo_categoria", "taxonomia_tipo_icao"])

    ocorrencia = data["ocorrencia_tipo"].to_list()

    total = transformar_em_dict(ocorrencia)

    print(f"O maior número de ocorrências ocorreu em função de: {incidencia(total)[0]}, com {total[incidencia(total)[0]]} ocorrências, representando { ((total[incidencia(total)[0]]) / (incidencia(total)[1])) * 100 }% dos casos")
    print(f"O total de acidentes foi: {incidencia(total)[1]}")

if __name__ == "__main__":
     main()








