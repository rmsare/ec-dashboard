import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource

from bokeh.layouts import column, row, gridplot
#from bokeh.palettes import ...


def meteo_tab(df):
    
    def get_dataset(src):
        df = src
        return ColumnDataSource(data=df)

    def style(p):

        return p

    def make_wind_plot(data):
        p = figure(x_axis_type='datetime', tools='hover,pan,box_zoom,reset', plot_height=300)
        p.scatter('date', 'wind_speed', source=data)
        p = style(p)
        return p

    def make_temp_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, tools='hover,pan,box_zoom,reset', plot_height=300)
        p.scatter('date', 'air_temperature', source=data)
        p = style(p)
        return p

    def make_pres_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, tools='hover,pan,box_zoom,reset', plot_height=300)
        p.scatter('date', 'air_pressure', source=data)
        p = style(p)
        return p

    def update(attr, old, new):
        pass

    src = get_dataset(df)
    wind_plot = make_wind_plot(src)
    temp_plot = make_temp_plot(src)
    pres_plot = make_pres_plot(src)

    #controls = WidgetBox(date_selection, filtering_select)
    layout = column(wind_plot, temp_plot, pres_plot)
    tab = Panel(child=layout, title='Meterology', width=1024)
    
    return tab
