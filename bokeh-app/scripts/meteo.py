import numpy as np
import pandas as pd

from scripts.utils import style

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource
from bokeh.models.widgets import Div

from bokeh.layouts import column, row, gridplot
#from bokeh.palettes import ...


def meteo_tab(source):

    def make_wind_plot(data):
        p = figure(x_axis_type='datetime', 
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='Wind speed [m/s]')
        p.scatter('date', 'wind_speed', size=5, color='black', fill_alpha=0.9, source=data)
        p = style(p)
        return p

    def make_temp_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='Temperature [K]')
        p.scatter('date', 'air_temperature', size=5, color='black', fill_alpha=0.9, source=data)
        p = style(p)
        return p

    def make_pres_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='Pressure [Pa]')
        p.scatter('date', 'air_pressure', size=5, color='black', fill_alpha=0.9, source=data)
        p = style(p)
        return p

    def update(attr, old, new):
        pass

    wind_plot = make_wind_plot(source)
    temp_plot = make_temp_plot(source)
    pres_plot = make_pres_plot(source)

    div = Div(text='', height=5)
    layout = column(wind_plot, temp_plot, pres_plot)
    tab = Panel(child=layout, title='Meterology', width=3000)
    
    return tab
