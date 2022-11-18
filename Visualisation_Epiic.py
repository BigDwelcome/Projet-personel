#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 08:18:43 2022

@author: douati
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

########### import database
df= pd.read_excel("Étude d’opinion Xylos (réponses).xlsx")
##### 1.exploratory data
##Objectif
#Compréhension des données

# taille des données : (353, 27) 
df.shape
# types de données
df.dtypes.value_counts()
##object            22
##float64            4
##datetime64[ns]     1

# Visualisation de la base de donné 
sns.heatmap(df.isna(), cbar=False)
# suppression des variables inutiles

(df.isna().sum()/df.shape[0]).sort_values(ascending=True)

