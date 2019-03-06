import numpy as np
import pandas as pd

from scripts.utils import plot_averages, style

from bokeh.plotting import figure
from bokeh.models import Panel, ColumnDataSource
from bokeh.models.widgets import Div

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def flux_tab(source):

    def make_co2_plot(source):
        p = figure(title='CO2 Flux', x_axis_type='datetime', tools='crosshair,hover,pan,box_zoom,reset',
                   y_range=[-5, 5000], plot_height=300, y_axis_label='CO2 flux [umol/m2s]')

        p.scatter('date', 'co2_flux', size=5, color='black', fill_alpha=0.9, legend='Data', source=source)

        p = plot_averages(source, p, 'co2_flux')
        p = style(p)

        return p
    
    def make_H_plot(source):
        p = figure(title='Sensible Heat Flux', x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='H [W/m2]')
        
        p.scatter('date', 'H',  size=5, color='black', fill_alpha=0.9, source=source)
                
        p = plot_averages(source, p, 'H')
        p = style(p)

        return p
    
    def make_LE_plot(source):
        p = figure(title='Latent Heat Flux', x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='LE [W/m2]')

        p.scatter('date', 'LE',  size=5, color='black', fill_alpha=0.9, source=source)
        
        p = plot_averages(source, p, 'H')
        p = style(p)

        return p

    def make_h2o_plot(source):
        p = figure(title='H2O Flux', x_axis_type='datetime', x_range=flux_plot.x_range,
                   tools='crosshair,hover,pan,box_zoom,reset', plot_height=300,
                   y_axis_label='H2O flux [umol/m2s]')
        
        p.scatter('date', 'h2o_flux',  size=5, color='black', fill_alpha=0.9, source=source)
               
        p = plot_averages(source, p, 'h2o_flux')
        p = style(p)

        return p

    def update(attr, old, new):
        pass

    flux_plot = make_co2_plot(source)
    H_plot = make_H_plot(source)
    LE_plot = make_LE_plot(source)
    h2o_plot = make_h2o_plot(source)

    div = Div(text='', height=5)
    layout = column(flux_plot, H_plot, LE_plot, h2o_plot)
    tab = Panel(child=layout, title='Fluxes', width=3000)
    
    return tab
