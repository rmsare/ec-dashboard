import pandas as pd

from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

from scripts.flux import flux_tab
from scripts.meteo import meteo_tab
from scripts.crossplot import crossplot_tab
from scripts.wind import wind_tab
from scripts.footprint import footprint_tab
from scripts.inversion import inversion_tab


df = pd.read_pickle('data/filtered.pk')

tab1 = flux_tab(df)
tab2 = meteo_tab(df)
tab3 = crossplot_tab(df)
tab4 = wind_tab(df)
tab5 = footprint_tab(df)
tab6 = inversion_tab(df)

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5, tab6])

curdoc().add_root(tabs)
