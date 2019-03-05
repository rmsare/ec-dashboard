import boto
import pandas as pd
import numpy as np


def download_data(bucket_name):
    pass

def filter_data(data):
    mask = (data.qc_co2_flux == 0) & (data.qc_H == 0) & \
           (data.qc_LE == 0) & (data['u*'] > 0.3)
    data = data.loc[mask]
    return data
    
def style(p):
    p.yaxis.axis_label_text_font_size = '16pt'
    p.xaxis.major_label_text_font_size = '14pt'
    p.yaxis.major_label_text_font_size = '14pt'
    return p
