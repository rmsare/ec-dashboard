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
