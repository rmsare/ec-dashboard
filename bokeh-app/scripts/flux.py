import numpy as np
import pandas as pd

from scripts.utils import style

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource
from bokeh.models.widgets import Div

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def flux_tab(df):

    def make_co2_plot(df):
        p = figure(x_axis_type='datetime', tools='crosshair,hover,pan,box_zoom,reset',
                   y_range=[-10, 5000], plot_height=300, y_axis_label='CO2 flux [umol/m2s]')

        p.scatter('date', 'co2_flux', size=10, line_color='white', color='black', fill_alpha=0.9, source=df)

        #df2 = pd.DataFrame(index=df['date'], data=df['co2_flux'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'co2_flux', size=10, line_color='white', color='b', fill_alpha=0.9, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'co2_flux', size=10, line_color='white', color='r', fill_alpha=0.9, source=seasonal)

        p = style(p)

        return p
    
    def make_h2o_plot(df):
        p = figure(x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='H2O flux [umol/m2s]')
        
        p.scatter('date', 'h2o_flux',  size=10, line_color='white', color='black', fill_alpha=0.9,source=df)
        
        #df2 = pd.DataFrame(index=df['date'], data=df['h2o_flux'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'h2o_flux', size=10, line_color='white', color='b', fill_alpha=0.9, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'h2o_flux', size=10, line_color='white', color='r', fill_alpha=0.9, source=seasonal)
       
        p = style(p)

        return p

    def make_H_plot(df):
        p = figure(x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='H [W/m2]')
        
        p.scatter('date', 'H',  size=10, line_color='white', color='black', fill_alpha=0.9,source=df)
        
        #df2 = pd.DataFrame(index=df['date'], data=df['H'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'H', size=10, line_color='white', color='b', fill_alpha=0.9, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'H', size=10, line_color='white', color='r', fill_alpha=0.9, source=seasonal)
        
        p = style(p)

        return p
    
    def make_LE_plot(df):
        p = figure(x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='LE [W/m2]')

        p.scatter('date', 'LE',  size=10, line_color='white', color='black', fill_alpha=0.9,source=df)

        #df2 = pd.DataFrame(index=df['date'], data=df['LE'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'LE', size=10, line_color='white', color='b', fill_alpha=0.9, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'LE', size=10, line_color='white', color='r', fill_alpha=0.9, source=seasonal)
        
        p = style(p)

        return p

    def update(attr, old, new):
        pass

    flux_plot = make_co2_plot(df)
    h2o_plot = make_h2o_plot(df)
    H_plot = make_H_plot(df)
    LE_plot = make_LE_plot(df)

    div = Div(text='', height=10)
    layout = column(flux_plot, h2o_plot, H_plot, LE_plot)
    tab = Panel(child=layout, title='Fluxes', width=3000)
    
    return tab
