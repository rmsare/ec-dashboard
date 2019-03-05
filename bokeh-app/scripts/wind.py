import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def wind_tab(df):
    
    def get_dataset(src):
        df = src
        return ColumnDataSource(data=df)

    def style(p):

        return p

    def make_speed_plot(data):
        p = figure(x_axis_type='datetime', tools='hover,pan,box_zoom,reset', plot_height=200)
        p.scatter('date', 'wind_speed', source=data)
        p = style(p)
        return p

    def make_dir_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, y_range=[-5, 365], tools='hover,pan,box_zoom,reset', plot_height=200)
        p.scatter('date', 'wind_dir', source=data)
        p.yaxis.ticker = [0, 90, 180, 270, 360]
        p = style(p)
        return p

    def make_ustar_plot(data):
        p = figure(x_axis_type='datetime', x_range=wind_plot.x_range, tools='hover,pan,box_zoom,reset', plot_height=200)
        p.scatter('date', 'u*', source=data)
        p = style(p)
        return p

    def update(attr, old, new):
        pass

    src = get_dataset(df)
    wind_plot = make_speed_plot(src)
    temp_plot = make_dir_plot(src)
    pres_plot = make_ustar_plot(src)

    #controls = WidgetBox(date_selection, filtering_select)
    layout = column(wind_plot, temp_plot, pres_plot)
    tab = Panel(child=layout, title='Wind', width=1024)
    
    return tab
