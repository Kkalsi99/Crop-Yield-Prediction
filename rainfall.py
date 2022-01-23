import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

raindata = pd.read_csv("dataset/rainfall in india 1901-2015.csv")
# print(raindata.head())
valid_states_rain = raindata[(raindata['SUBDIVISION'] == 'BIHAR') | (raindata['SUBDIVISION']=='KERALA') | (raindata['SUBDIVISION']=='ARUNACHAL PRADESH')|(raindata['SUBDIVISION']=='TAMIL NADU')|(raindata['SUBDIVISION']=='UTTARAKHAND')|(raindata['SUBDIVISION']=='ORISSA')|(raindata['SUBDIVISION']=='HIMACHAL PRADESH')|(raindata['SUBDIVISION']=='LAKSHADWEEP')|(raindata['SUBDIVISION']=='PUNJAB')|(raindata['SUBDIVISION']=='CHHATTISGARH')|(raindata['SUBDIVISION']=='ANDAMAN & NICOBAR ISLANDS')|(raindata['SUBDIVISION']=='JHARKHAND')]
# print(set(valid_states_rain['SUBDIVISION']))
print(valid_states_rain.head())
valid_states_rain = valid_states_rain[['SUBDIVISION','YEAR','Jun-Sep']]
print(valid_states_rain)
# print(valid_states_rain.describe())
valid_states_rain = valid_states_rain[valid_states_rain['YEAR']>1996]
valid_states_rain.columns = ['State','Year','Rainfall']
# print
valid_states_rain = valid_states_rain[valid_states_rain.State != 'LAKSHADWEEP']
valid_states_rain = valid_states_rain.replace('UTTARAKHAND','Uttarakhand')
valid_states_rain = valid_states_rain.replace('ORISSA','Odisha')
valid_states_rain = valid_states_rain.replace('HIMACHAL PRADESH','Himachal Pradesh')
valid_states_rain = valid_states_rain.replace('JHARKHAND','Jharkhand')
valid_states_rain = valid_states_rain.replace('ARUNACHAL PRADESH','Arunachal Pradesh')
valid_states_rain = valid_states_rain.replace('TAMIL NADU','Tamil Nadu')
valid_states_rain = valid_states_rain.replace('CHHATTISGARH','Chhattisgarh')
# valid_states_rain = valid_states_rain.replace('JAMMU & KASHMIR','Jammu and Kashmir')
valid_states_rain = valid_states_rain.replace('ANDAMAN & NICOBAR ISLANDS','Andaman and Nicobar Islands')
valid_states_rain = valid_states_rain.replace('BIHAR','Bihar')
valid_states_rain = valid_states_rain.replace('PUNJAB','Punjab')
valid_states_rain = valid_states_rain.replace('KERALA','Kerala')

def get_rain_data():
    return valid_states_rain
