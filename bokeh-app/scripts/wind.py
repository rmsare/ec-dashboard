import numpy as np
import pandas as pd

from scripts.utils import style

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource
from bokeh.models.widgets import Div

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def wind_tab(df):
    
    def get_dataset(src):
        df = src
        return ColumnDataSource(data=df)

    def make_speed_plot(data):
        p = figure(x_axis_type='datetime', tools='crosshair,hover,pan,box_zoom,reset', plot_height=300, y_axis_label='Wind speed [m/s]')
        p.scatter('date', 'wind_speed', size=10, line_color='white', color='black', fill_alpha=0.9, source=data)
        p = style(p)
        return p

    def make_dir_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, y_range=[-5, 365], tools='crosshair,hover,pan,box_zoom,reset', plot_height=300, y_axis_label='Wind direction [deg from N]')
        p.scatter('date', 'wind_dir', size=10, line_color='white', color='black', fill_alpha=0.9, source=data)
        p.yaxis.ticker = [0, 90, 180, 270, 360]
        p = style(p)
        return p

    def make_ustar_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, tools='crosshair,hover,pan,box_zoom,reset', plot_height=300, y_axis_label='Frictional velocity (u*) [m/s]')
        p.scatter('date', 'u*', size=10, line_color='white', color='black', fill_alpha=0.9, source=data)
        p = style(p)
        return p

    def update(attr, old, new):
        pass

    src = get_dataset(df)
    wind_plot = make_speed_plot(src)
    temp_plot = make_dir_plot(src)
    pres_plot = make_ustar_plot(src)
    
    div = Div(text='', height=10)
    layout = column(wind_plot, temp_plot, pres_plot)
    tab = Panel(child=layout, title='Wind', width=3000)
    
    return tab
