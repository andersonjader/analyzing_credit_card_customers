import os
from pathlib import Path
from pandas import *


def pegarCaminho(arq):

    root = Path().resolve().parent
    p = os.path.join(root,arq)
    return p

def Salvar_planilha_dados_em_Data(df, nome):
    """
    Essa função recebe um datafreme como parametro e o nome do arquivo
    e salva os dados em uma planilha excel no diretorio data
    """
    n = 'data/' + nome + '.xlsx'
    caminho = pegarCaminho(n)
    df.to_excel(caminho, index = False)
