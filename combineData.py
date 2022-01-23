import rainfall
import crop
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

valid_states_rain = rainfall.get_rain_data()
valid_states_crop = crop.get_crops_data()

Rainfall_list = [0] * 75555
valid_states_crop['Rainfall'] = Rainfall_list
valid_states_crop['Yield'] = Rainfall_list
states_set = set(valid_states_crop['State'])
year_set = set(valid_states_crop['Year'])
# print(list(valid_states_crop[valid_states_crop['State'] == "Jammu and Kashmir"]['Year']))
print(valid_states_crop.columns)
for state in states_set:
    # print(state)
    for year in year_set:
        # print(valid_states_crop[valid_states_crop['State'] == state]['Year'])
        if (year in list(valid_states_crop[valid_states_crop['State'] == state]['Year'])):
            # print(state,year)
            valid_states_crop.loc[(valid_states_crop['State'] == state) & \
                                  (valid_states_crop['Year'] == year), 'Rainfall'] = \
                list(valid_states_rain[(valid_states_rain['State'] == state) & \
                                       (valid_states_rain['Year'] == year)]['Rainfall'])[0]
            valid_states_crop.loc[(valid_states_crop['State'] == state) & \
                                  (valid_states_crop['Year'] == year), 'Yield'] = valid_states_crop['Production'] / \
                                                                                  valid_states_crop['Area']
            valid_states_crop.loc[(valid_states_crop['State'] == state) & \
                                  (valid_states_crop['Year'] == year), 'Production'] = valid_states_crop['Production'] / \
                                                                                  1000
crop_data_alpha = valid_states_crop.dropna()
# print(valid_states_crop)
# crop_data_alpha = crop_data_alpha[crop_data_alpha.Production != 0.0]
# print(crop_data_alpha.head())
# print(set(crop_data_alpha['Season']))
# crop_data_alpha = crop_data_alpha.drop('State', axis=1)
# crop_data_alpha = crop_data_alpha.drop('Year', axis=1)
# crop_data_alpha = crop_data_alpha.sort_values(by='Crop')
# crop_data_alpha = crop_data_alpha.reset_index(drop=True)
# # print(crop_data_alpha.head())
kharif_data = crop_data_alpha[crop_data_alpha['Season'] == 'Kharif     ']
# kharif_data = kharif_data[kharif_data['State']=="Punjab"]


# print(wheat_data)
# print(wheat_data.head())
# print(wheat_data[wheat_data['Production'] == 3.0])
# plt.scatter(wheat_data['Production'], wheat_data['Rainfall'])
# potato_data = crop_data_alpha[crop_data_alpha['Crop'] == 'Potato']
# plt.scatter(potato_data['Production'], potato_data['Rainfall'])
# plt.scatter(kharif_data['Production'],kharif_data['Rainfall'])
# plt.show()


def Dataset():
    return kharif_data
