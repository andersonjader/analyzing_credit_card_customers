import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns

def norm_Data(df,col):
  """
  função que normaliza os dados e retorna um dataframe
  parametros: df: dataframe, col: colunas selecionadas
  """
  df_norm = StandardScaler().fit_transform(df)
  df2 = pd.DataFrame(data=df_norm, columns=col)
  return df2

def correlacao(df):
  df2 = df.corr().style.background_gradient(cmap='Blues')
  return df2

def correlacao_map(df, caminho):
  fig, ax = plt.subplots(figsize=(12,8))
  sns.heatmap(df.corr(), cmap='Blues', linewidths= 0.5, annot=True)
  #plt.savefig(caminho,dpi = 300)

def calc_qtde_outliers(dataframe, col):
  q1 = dataframe[col].quantile(0.25)
  q3 = dataframe[col].quantile(0.75)
  FIQ = q3 - q1
  f_baixo = q1 - 1.5*FIQ
  f_alta = q3 - 1.5*FIQ
  f1 = dataframe[col] > f_alta
  f2 = dataframe[col] < f_baixo
  d_alto = dataframe[f1]
  d_baixo = dataframe[f2]
  t_a = d_alto[col].count()
  t_b = d_baixo[col].count()
  return t_a, t_b