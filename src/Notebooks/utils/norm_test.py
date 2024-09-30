import pandas as pd
from scipy import stats
from scipy.stats import anderson

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

def cal_Anderson_Darling(data,a):
    p = anderson(data).statistic
    if p < a:
        r = 'non-standard distribution'
        return r
    else:
        r = 'standard distribution'
        return r

def dagostinho(data,a):

    _, p = stats.normaltest(data)
    if p < a:
        r = 'non-standard distribution'
        return r
    else:
        r = 'standard distribution'
        return r

def distribuitionGaus(data, name):
    #densidade, método kdeplot para densidade
    sns.kdeplot(data, color='blue').set(title=name)