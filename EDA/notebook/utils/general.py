import os
from pathlib import Path
from pandas import *


def catchPath(arq):

    root = Path().resolve().parent
    p = os.path.join(root,arq)
    return p

def SaveDataFrame(df, name):
    """
    This function receives a datafreme as a parameter and the file name and 
    saves the data in an excel spreadsheet in the data directory
    """
    n = 'data/' + name + '.xlsx'
    p = catchPath(n)
    df.to_excel(p, index = False)
