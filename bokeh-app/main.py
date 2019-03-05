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

src, tab1 = filter_tab()
tab2 = flux_tab(src)
tab3 = meteo_tab(src)
tab4 = wind_tab(src)
#tab5 = crossplot_tab(df)

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])

curdoc().add_root(tabs)
curdoc().title = 'USGS EC Station'
