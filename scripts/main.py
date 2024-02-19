import os
import pandas as pd


def ler_arquvios_xls(pasta_dados):
        dados = []
        for arquivo in os.listdir(pasta_dados):
            if arquivo.endswith('.xlsx'):
                caminho_arquivo =  os.path.join(pasta_dados, arquivo)
                print(f"Lendo arquivos: {caminho_arquivo}")
                df = pd.read_excel(arquivo)
                dados.append(df)
        return dados

def main():
    pasta_dados = "C:\\Users\\Pointer 01\\Downloads\\data_implantation_analysis\\data"
    dados = ler_arquvios_xls(pasta_dados)

    if not pasta_dados:
        print("Caminho não encontrado!")

    if not dados:
        print("Nenhum arquivo Excel encontrado na pasta.")
        return
           

    for df in dados:
        print("DataFrame:")
        print(df.info())

    if __name__=="__main__":
           main()
