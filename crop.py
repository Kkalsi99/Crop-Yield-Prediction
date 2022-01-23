import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
cropdata = pd.read_csv("dataset/crop_production.csv")
cropdata.columns = ['State', 'District_Name', 'Year', 'Season', 'Crop', 'Area',
       'Production']
# print(cropdata.columns)
valid_states_crop = cropdata[(cropdata['State']=='Bihar') | (cropdata['State']=='Kerala') | (cropdata['State']=='Arunachal Pradesh')|(cropdata['State']=='Tamil Nadu')|(cropdata['State']=='Uttarakhand')|(cropdata['State']=='Odisha')|(cropdata['State']=='Himachal Pradesh')|(cropdata['State']=='Punjab')|(cropdata['State']=='Chhattisgarh')|(cropdata['State']=='Andaman and Nicobar Islands')|(cropdata['State']=='Jharkhand')]
# print(valid_states_crop)
# valid_states_rain = valid_states_rain.replace('ORISSA','Odisha')


def get_crops_data():
    return valid_states_crop