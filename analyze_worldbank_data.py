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

#%%

#Create a scatterplot of the relationship between infant mortality and GDP per Capita:

x = world_bank['GDP_PC']
y = world_bank['Inf_MR']

plt.scatter(x, y)
plt.title('Infant Mortality vs GDP Per Capita', fontsize = 12)
plt.xlabel('GDP Per Capita', fontsize = 8)
plt.ylabel('Infant Mortality Rate', fontsize = 8)
plt.show()
plt.savefig('Infant_GDP_corr.png')
plt.close()
#%%

#Create a scatterplot of the relationship between infant mortality and adolescent fertility rate:

a = world_bank['Adol_FR']
b = world_bank['Inf_MR']

plt.scatter(a, b)
plt.title('Infant Mortality vs Adolescent Fertility Rate', fontsize = 12)
plt.xlabel('Adolescent Fertility Rate', fontsize = 8)
plt.ylabel('Infant Mortality Rate', fontsize = 8)
plt.show()
plt.savefig('Infant_Adol-FR_corr.png')
plt.close()
#%%

#Create a scatterplot of the relationship between infant mortality and communicable diseases:

c = world_bank['%_Mort_C']
d = world_bank['Inf_MR']

plt.scatter(c, d)
plt.title('Infant Mortality vs % Mortality Communicable Disease', fontsize = 12)
plt.xlabel('% Mortality Communicable Disease', fontsize = 8)
plt.ylabel('Infant Mortality Rate', fontsize = 8)
plt.show()
plt.savefig('Infant_Comm_corr.png')
plt.close()

#%%

#Calculate the correlations between infant mortality rates and the other variables:

corr = (world_bank['Inf_MR'].corr(world_bank['GDP_PC'])).round(5)
print('\nThe correlation between infant morality and GDP per Capita in South America in 2016 is:', corr)

corr1 = (world_bank['Inf_MR'].corr(world_bank['%_Mort_C'])).round(5)
print('\nThe correlation between infant mortality and percent of total deaths caused by communicable diseases is:', corr1)

corr2 = (world_bank['Inf_MR'].corr(world_bank['Adol_FR'])).round(5)
print('\nThe correlation between infant mortality and adolescent fertility rate is:', corr2)


#%%
#Create a correlation matrix heatmap with all the variables:

sns.set(font_scale=1.8)
plt.figure(figsize = (20,15))
sns_plot = sns.heatmap(world_bank.corr(), annot = True, cmap = 'coolwarm',square = True, annot_kws={'size':24})
sns_plot.figure.savefig('Correlation_matrix.png')

#%%

#Save csv as a dta file for analysis in STATA:

world_bank.to_stata('worldbank_data.dta')


