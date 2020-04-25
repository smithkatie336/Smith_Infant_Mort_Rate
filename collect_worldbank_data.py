# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:17:56 2020

@author: smith
"""

import requests
import pandas as pd
import json

#Retrieve infant mortality data from worldbank.org for South American countries in 2016:

SA_countries = ['ARG','BOL','BRA','CHL','COL','ECU','GUY','PRY','PER','SUR','URY','VEN']

inf_mort = dict()

for count in SA_countries:
    api = 'https://api.worldbank.org/v2/country/'+count+'/indicator/SP.DYN.IMRT.IN?date=2016&format=JSON'
    response = requests.get(api)
    mort = json.loads(response.text)
    mort = mort[1][0]
    i_mort = [mort['country']['value'],mort['value']]
    inf_mort.update({count: i_mort})

#Create a DataFrame of country name and infant mortality rate data

colnames = ['Country','Inf_MR']
datarows = inf_mort.values()
i_m_rate = pd.DataFrame(columns=colnames, data=datarows)


#%%

#Retrieve data for percent of deaths by communicable diseases from worldbank.org for South American countries in 2016:

SA_countries = ['ARG','BOL','BRA','CHL','COL','ECU','GUY','PRY','PER','SUR','URY','VEN']

mort_comm = dict()

for count in SA_countries:
    api = 'https://api.worldbank.org/v2/country/'+count+'/indicator/SH.DTH.COMM.ZS?date=2016&format=JSON'
    response = requests.get(api)
    m_com = json.loads(response.text)
    m_com = m_com[1][0]
    mortcom = [m_com['country']['value'],m_com['value']]
    mort_comm.update({count: mortcom})

#Create a DataFrame of country name and percent of deaths by communicable diseases data

colnames = ['Country','%_Mort_C']
datarows = mort_comm.values()
per_mort_comm = pd.DataFrame(columns=colnames, data=datarows)


#%%
   
#Retrieve GDP per Capita from worldbank.org for South American countries in 2016:

SA_countries = ['ARG','BOL','BRA','CHL','COL','ECU','GUY','PRY','PER','SUR','URY','VEN']

GDP_per_cap = dict()

for count in SA_countries:
    api = 'https://api.worldbank.org/v2/country/'+count+'/indicator/NY.GDP.PCAP.PP.CD?date=2016&format=JSON'
    response = requests.get(api)
    gpc = json.loads(response.text)
    gpc = gpc[1][0]
    GDP_pc = [gpc['country']['value'],gpc['value']]
    GDP_per_cap.update({count: GDP_pc})

#Create a DataFrame of country name and GDP Per Capita data

colnames = ['Country','GDP_PC']
datarows = GDP_per_cap.values()
GDP_percapita = pd.DataFrame(columns=colnames, data=datarows)

    
#%%  

#Use an API call to retrieve adolescent fertility rate from worldbank.org for South American countries in 2016:

SA_countries = ['ARG','BOL','BRA','CHL','COL','ECU','GUY','PRY','PER','SUR','URY','VEN']

fert_rate = dict()

for count in SA_countries:
    api = 'https://api.worldbank.org/v2/country/'+count+'/indicator/SP.ADO.TFRT?date=2016&format=JSON'
    response = requests.get(api)
    fr = json.loads(response.text)
    fr = fr[1][0]
    f_rate = [fr['country']['value'],fr['value']]
    fert_rate.update({count: f_rate})

#Create a DataFrame of country name and adolescent fertility rate data

colnames = ['Country','Adol_FR']
datarows = fert_rate.values()
adol_fert_rate = pd.DataFrame(columns=colnames, data=datarows)


#%%

#Merge datasets to create 'South_America_data' DataFrame and set index to 'Country':

d1 = pd.merge(i_m_rate, per_mort_comm, on = 'Country')
d2 = pd.merge(d1, GDP_percapita, on = 'Country')
worldbank_data = pd.merge(d2, adol_fert_rate, on = 'Country')

#Create a column for country names that is uppercase for future analysis and remove 'RB' from Venezuela:

worldbank_data['Country'] = worldbank_data['Country'].str.upper()
worldbank_data['Country'].replace('VENEZUELA, RB', 'VENEZUELA', inplace = True)

#Set index
worldbank_data.set_index('Country', inplace=True)

#Save DataFrame as 'worldbank_data.csv':

worldbank_data.to_csv('worldbank_data.csv')


