import os
import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource


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
    df = df.iloc[0:3000]
    df.index.name = 'date' 
    return df

def plot_averages(source, plot, var):

    palette = ["#718dbf", "#e84d60"]
    

    daily = pd.DataFrame(index=source.data['date'], data=source.data[var]).resample('1D').mean()
    daily.index.name = 'date'
    data = {'date': daily.index, var: daily.values}
    src = ColumnDataSource(data)
    plot.line('date', var, line_width=3, line_color=palette[0], legend='Daily', source=src)

    seasonal = pd.DataFrame(index=source.data['date'], data=source.data[var]).resample('120D').mean()
    seasonal.index.name = 'date'
    data = {'date': seasonal.index, var: seasonal.values}
    src = ColumnDataSource(data)
    plot.line('date', var, line_width=3, line_color=palette[1], legend='Seasonal', source=src)

    return plot

def style(p):
    p.yaxis.axis_label_text_font_size = '16pt'
    p.xaxis.major_label_text_font_size = '14pt'
    p.yaxis.major_label_text_font_size = '14pt'
    return p
