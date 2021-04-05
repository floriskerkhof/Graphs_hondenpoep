# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 10:06:18 2021

@author: flori
"""

import pandas as pd
import requests
import cbsodata 
import numpy as np
import matplotlib as mpl
import datetime



import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


import Functions as fl

#fl.loadin_cbsdata('82242NED')
data_overlast=fl.loadin_cbsdata('81924NED')
data_overlast_adj=data_overlast[data_overlast['Marges']=='Waarde']

filter_list=['gemeente','PD','BT','PV','RE','Gemeenten','LD','G4','G32','G40']
# bt is basisteam politie
# pv is provincie
# pd is politie district
# re is regionale eenheid
# LD is landsdeel
for i in filter_list:
    data_overlast_adj=data_overlast_adj[~data_overlast_adj['RegioS'].str.contains(i)]
data_overlast_adj=data_overlast_adj[data_overlast_adj['Perioden']!='2012']

hondenpoep=data_overlast_adj.loc[:,['RegioS','Perioden','Hondenpoep_35']]

fl.make_graph(hondenpoep,'RegioS','Perioden','Hondenpoep_35','Vaak last van hondenpoep per gemeenten')
# fl.make_graph(data_faillissementen,'TypeGefailleerde','date','UitgesprokenFaillissementen_1','Aantal Faillissementen')

data_overlast_adj=data_overlast[data_overlast['RegioS'].str.contains('PV')]
data_overlast_adj=data_overlast_adj[data_overlast_adj['Perioden']!='2012']
data_overlast_adj=data_overlast_adj[data_overlast_adj['Marges']=='Waarde']
hondenpoep_provincie=data_overlast_adj.loc[:,['RegioS','Perioden','Hondenpoep_35']]

fl.make_graph(hondenpoep_provincie,'RegioS','Perioden','Hondenpoep_35','Vaak last van hondenpoep per gemeenten')


import plotly.express as px
from plotly.offline import plot


fig = px.line(hondenpoep_provincie, x="Perioden", y="Hondenpoep_35", color='RegioS', title='Hondenpoep provincie',
              labels={'RegioS':'Provincie','Hondenpoep_35':'Aandeel veel last van hondenpoep'}
                 )
fig.show()
plot(fig)