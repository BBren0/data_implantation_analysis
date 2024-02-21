import os
import pandas as pd


def ler_arquvios_xls(pasta_dados):
        dados = []
        for arquivo in os.listdir(pasta_dados):
            caminho_arquivo =  os.path.join(pasta_dados, arquivo)
            if arquivo.endswith('.xlsx'):
                print(f"Lendo arquivos: {caminho_arquivo}")
                df = pd.read_excel(caminho_arquivo, sheet_name=None)
                dados.append(df)
            else:
                print(f"\n\nArquivo não encontrado em:{caminho_arquivo}\t\n")

        return dados


def verificar_analistas(dados, analistas):
    for dicionario in dados:
        for nome_planilhas, df in dicionario.items():
                    if nome_planilhas.startswith('Checklist'):
                        celula = df.iloc[2,6]
                        analistas.append(celula)
                        print(f"\n DataFrame da planilha do '{nome_planilhas}'")
                        print(df.head())
                        print("\n")
                        print("\nInformações do DataFrame:")
                        print(df.info())
                        print("\n")
                        print("\nRótulo das Colunas")
                        print(df.columns)
                        print("\nRótulo das Linhas")
                        print(df.shape[0])
                        print(f"Nome do analista: {celula}")


    print(f"Os analistas que estão com importação são: {analistas} ")
 

def verificar_status_conclusão(dados):
    PRIMEIRO_CT_TOTAL = 7
    TREINAMENTO_TOTAL = 11
    IMPORTAÇÃO_TOTAL = 18
    HOMOLOG_TOTAL = 2

    for dicionario in dados:
        for nome_planilhas, df in dicionario.items():
            if nome_planilhas.startswith('Checklist'):
                conteudo_coluna = df[df.columns[1]]
                conteudo_coluna2 = df[df.columns[1]]
                print(conteudo_coluna)

                for indice in conteudo_coluna:
                    if indice == "1.00":
                         print("")
                     




    



def main():
    pasta_dados = "C:\\Users\\Pointer 01\\Downloads\\data_implantation_analysis\\data"
    if not pasta_dados:
        print("Caminho não encontrado!")

    dados = ler_arquvios_xls(pasta_dados)
    if not dados:
        print("\n\nNenhum arquivo Excel encontrado na pasta.\n\n")
        return
    

    analistas = []
    verificar_analistas(dados, analistas)

    verificar_status_conclusão(dados)

            
if __name__=="__main__":
    main()
