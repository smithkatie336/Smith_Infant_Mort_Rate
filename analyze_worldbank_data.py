# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:05:40 2020

@author: smith
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Load 'worldbank_data.csv' dataset:

world_bank = pd.read_csv('worldbank_data.csv', index_col = 'Country')
print(world_bank[:5])

#%%
#Confirm previous study results by checking correlation between infant mortality and GDP per Capita:

corr = (world_bank['Inf_MR'].corr(world_bank['GDP_PC'])).round(5)
print('\nThe correlation between infant morality and GDP per Capita in South America in 2016 is:', corr)

#Create a scatterplot of the relationship between infant mortality and GDP per Capita:

x = world_bank['GDP_PC']
y = world_bank['Inf_MR']

plt.scatter(x, y)
plt.title('Relationship between Infant Mortality and GDP Per Capita')
plt.xlabel('GDP Per Capita')
plt.ylabel('Infant Mortality Rate')
plt.show()
plt.savefig('Infant_GDP_corr.png')

#%%

#Create a scatterplot of the relationship between infant mortality and adolescent fertility rate:

a = world_bank['Adol_FR']
b = world_bank['Inf_MR']

plt.scatter(a, b)
plt.title('Infant Mortality vs Adolescent Fertility Rate', fontsize = 14)
plt.xlabel('Adolescent Fertility Rate', fontsize = 12)
plt.ylabel('Infant Mortality Rate', fontsize = 12)
plt.show()
plt.savefig('Infant_Adol-FR_corr.png')

#%%

#Create a scatterplot of the relationship between infant mortality and communicable diseases:

c = world_bank['%_Mort_C']
d = world_bank['Inf_MR']

plt.scatter(c, d)
plt.title('Infant Mortality vs % Mortality Communicable Disease', fontsize = 14)
plt.xlabel('% Mortality Communicable Disease', fontsize = 12)
plt.ylabel('Infant Mortality Rate', fontsize = 12)
plt.show()
plt.savefig('Infant_Comm_corr.png')

#%%

#Create a scatterplot of the relationship between GDP Per Capita and communicable diseases:

e = world_bank['GDP_PC']
f = world_bank['%_Mort_C']

plt.scatter(e, f)
plt.title('GDP Per Capita vs % Mortality Communicable Disease', fontsize = 14)
plt.xlabel('GDP Per Capita', fontsize = 12)
plt.ylabel('% Mortality Communicable Disease', fontsize = 12)
plt.show()
plt.savefig('GDP_Comm_corr.png')

#%%
#Create a correlation matrix with all the variables

print('\n')
corr_all = world_bank.corr()
print('\nCorrelation maxtrix:')
print(corr_all)

sns.set(font_scale=1.4)
plt.figure(figsize = (20,12))
sns.heatmap(world_bank.corr(), annot = True, cmap = 'coolwarm',square = True, annot_kws={'size':16})

#%%

world_bank.to_stata('worldbank_data.dta')


