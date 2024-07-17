import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns

def QQplot(data):
    fig, ax = plt.subplots()
    stats.probplot(data, fit=True,   plot=ax)
    plt.title('QQplot')
    plt.show()

def calcShapiro(data):
    r = stats.shapiro(data)
    return r[1]

def distribuitionGaus(data, name):
    #densidade, método kdeplot para densidade
    sns.kdeplot(data, color='blue').set(title=name)