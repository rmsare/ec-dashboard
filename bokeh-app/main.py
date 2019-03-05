import os
import pandas as pd

from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

from scripts.filter import filter_tab
from scripts.flux import flux_tab
from scripts.meteo import meteo_tab
#from scripts.crossplot import crossplot_tab
from scripts.wind import wind_tab

#from scripts.settings import STATIONS
from scripts.utils import download_data, filter_data

#print('Downloading data from S3...')
#download_data(station_name)

#print('QC filtering data...')
df = pd.read_pickle(os.path.join(os.path.dirname(__file__), 'data/master.pk'))
df = filter_data(df)
df = df.iloc[0:100]
df.index.name = 'date'

df, tab1 = filter_tab(df)
tab2 = flux_tab(df)
tab3 = meteo_tab(df)
tab4 = wind_tab(df)
#tab5 = crossplot_tab(df)

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])

curdoc().add_root(tabs)
curdoc().title = 'USGS EC Station'
