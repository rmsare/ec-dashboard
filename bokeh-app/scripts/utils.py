import os
import pandas as pd
import numpy as np


def download_data(bucket_name):
    pass

def filter_data(data):
    mask = (data.qc_co2_flux == 0) & (data.qc_H == 0) & \
           (data.qc_LE == 0)
    data = data.loc[mask]
    return data

def read_data():
    df = pd.read_pickle(os.path.join(os.path.dirname(__file__), '../data/master.pk'))
    df = filter_data(df)
    df = df.iloc[0:1000]
    df.index.name = 'date' 
    return df

def style(p):
    p.yaxis.axis_label_text_font_size = '16pt'
    p.xaxis.major_label_text_font_size = '14pt'
    p.yaxis.major_label_text_font_size = '14pt'
    return p
