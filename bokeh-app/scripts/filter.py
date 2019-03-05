import os
import numpy as np
import pandas as pd

from scripts.utils import filter_data, read_data, style

from datetime import date

from bokeh.plotting import figure, show
from bokeh.models import Panel, ColumnDataSource, Range1d
from bokeh.models.layouts import WidgetBox
from bokeh.models.widgets import Button, CheckboxButtonGroup, DatePicker, TextInput

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def filter_tab():
        
    df = read_data()
    src = ColumnDataSource(df)

    fig = figure(x_axis_type='datetime', tools='crosshair,hover,pan,box_zoom,reset',
               y_range=[-10, 5000], plot_height=300, y_axis_label='CO2 flux [umol/m2s]')

    plot = fig.scatter('date', 'co2_flux', size=10, line_color='white', color='black', fill_alpha=0.9, source=src)
    fig = style(fig)

    dates = list(map(pd.to_datetime, df.index.values))

    min_date = DatePicker(title='Start date',
                             min_date=min(dates),
                             max_date=max(dates),
                             value=min(dates))
    max_date = DatePicker(title='End date',
                             min_date=min(dates),
                             max_date=max(dates),
                             value=max(dates))
    ustar = TextInput(title='Minimum u*', value='0.3')
    daynight = CheckboxButtonGroup(labels=['Daytime', 'Nighttime'], active=[0, 1])
    update = Button(label='Update', button_type='success')

    def update_data():
        df = read_data()
        
        df = df.loc[(df.index > pd.to_datetime(min_date.value)) & \
                    (df.index < pd.to_datetime(max_date.value))]

        df = df.loc[df['u*'] > float(ustar.value)]
        
        if daynight.active == []:
            df = pd.DataFrame([])
        elif daynight.active == [0]:
            df = df.loc[df.daytime == 1]
        elif daynight.active == [1]:
            df = df.loc[df.daytime == 0]
        elif daynight.active == [0, 1]:
            df = df.loc[(df.daytime == 1) | (df.daytime == 0)]

        print(daynight.active, ustar.value, min_date.value, max_date.value)
        
        src = ColumnDataSource(df)
        plot.data_source.data = src.data

    update_data()

    update.on_click(update_data)

    controls = column(WidgetBox(min_date, max_date),
                      ustar,
                      daynight,
                      update)
    layout = row(controls, fig)
    tab = Panel(child=layout, title='Filtering', width=3000)
    
    return src, tab
