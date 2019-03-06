import numpy as np
import pandas as pd

from scripts.utils import plot_averages, style

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource
from bokeh.models.widgets import Div

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def wind_tab(source):

    def make_speed_plot(source):
        p = figure(x_axis_type='datetime', tools='crosshair,hover,pan,box_zoom,reset', plot_height=300, y_axis_label='Wind speed [m/s]')
        p.scatter('date', 'wind_speed', size=5, color='black', fill_alpha=0.9, source=source)
        p = plot_averages(source, p, 'wind_speed')
        p = style(p)
        return p

    def make_dir_plot(source):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, y_range=[-5, 365], tools='crosshair,hover,pan,box_zoom,reset', plot_height=300, y_axis_label='Wind direction [deg from N]')
        p.scatter('date', 'wind_dir', size=5, color='black', fill_alpha=0.9, source=source)
        p = plot_averages(source, p, 'wind_dir')
        p.yaxis.ticker = [0, 90, 180, 270, 360]
        p = style(p)
        return p

    def make_ustar_plot(source):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, tools='crosshair,hover,pan,box_zoom,reset', plot_height=300, y_axis_label='Frictional velocity (u*) [m/s]')
        p.scatter('date', 'u*', size=5, color='black', fill_alpha=0.9, source=source)
        p = plot_averages(source, p, 'u*')
        p = style(p)
        return p

    wind_plot = make_speed_plot(source)
    temp_plot = make_dir_plot(source)
    pres_plot = make_ustar_plot(source)
    
    div = Div(text='', height=5)
    layout = column(wind_plot, temp_plot, pres_plot)
    tab = Panel(child=layout, title='Wind', width=3000)
    
    return tab
