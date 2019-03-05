import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def flux_tab(df):
    
    def style(p):

        return p

    def make_co2_plot(df):
        p = figure(x_axis_type='datetime', tools='hover,pan,box_zoom,reset',
                   y_range=[-10, 5000], plot_height=300)

        p.scatter('date', 'co2_flux', color='k', alpha=0.5, source=df)

        #df2 = pd.DataFrame(index=df['date'], data=df['co2_flux'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'co2_flux', color='b', alpha=0.5, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'co2_flux', color='r', alpha=0.5, source=seasonal)

        p = style(p)

        return p
    
    def make_h2o_plot(df):
        p = figure(x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='hover,pan,box_zoom,reset', plot_height=300)
        
        p.scatter('date', 'h2o_flux', source=df)
        
        #df2 = pd.DataFrame(index=df['date'], data=df['h2o_flux'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'h2o_flux', color='b', alpha=0.5, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'h2o_flux', color='r', alpha=0.5, source=seasonal)
       
        p = style(p)

        return p

    def make_H_plot(df):
        p = figure(x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='hover,pan,box_zoom,reset', plot_height=300)
        
        p.scatter('date', 'H', source=df)
        
        #df2 = pd.DataFrame(index=df['date'], data=df['H'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'H', color='b', alpha=0.5, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'H', color='r', alpha=0.5, source=seasonal)
        
        p = style(p)

        return p
    
    def make_LE_plot(df):
        p = figure(x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='hover,pan,box_zoom,reset', plot_height=300)

        p.scatter('date', 'LE', source=df)

        #df2 = pd.DataFrame(index=df['date'], data=df['LE'])
        #daily = ColumnDataSource(df2.rolling('1D').mean())
        #p.line('date', 'LE', color='b', alpha=0.5, source=daily)

        #seasonal = ColumnDataSource(df2.rolling('120D').mean())
        #p.line('date', 'LE', color='r', alpha=0.5, source=seasonal)
        
        p = style(p)

        return p

    def update(attr, old, new):
        pass

    flux_plot = make_co2_plot(df)
    h2o_plot = make_h2o_plot(df)
    H_plot = make_H_plot(df)
    LE_plot = make_LE_plot(df)

    #controls = WidgetBox(date_selection, filtering_select)
    layout = column(flux_plot, h2o_plot, H_plot, LE_plot)
    tab = Panel(child=layout, title='Fluxes', width=1024)
    
    return tab
