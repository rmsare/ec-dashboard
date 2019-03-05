import numpy as np
import pandas as pd

from datetime import date

from bokeh.plotting import figure, show
from bokeh.models import Panel, ColumnDataSource, Range1d
from bokeh.models.layouts import WidgetBox
from bokeh.models.widgets import DatePicker, TextInput

from bokeh.layouts import column, row
#from bokeh.palettes import ...


def filter_tab(df):
    
    def get_dataset(src):
        df = src
        return ColumnDataSource(data=df)

    def style(p):
        return p

    def make_plot(src):
        p = figure(x_axis_type='datetime', y_range=[-10, 5000])
        p.scatter('date', 'co2_flux', source=src)
        p = style(p)

        return p

    src = get_dataset(df)
    dates = list(map(pd.to_datetime, src.data['date']))

    plot = make_plot(src)

    min_date = DatePicker(title='Start date',
                             min_date=min(dates),
                             max_date=max(dates),
                             value=min(dates))
    max_date = DatePicker(title='End date',
                             min_date=min(dates),
                             max_date=max(dates),
                             value=max(dates))

    # filter = ...
    # daytime = ...

    def update_plot(attr, old, new):
        plot.x_range.bounds = [pd.to_datetime(min_date.value), pd.to_datetime(max_date.value)]

    for wid in [min_date, max_date]:
        wid.on_change('value', update_plot)

    controls = WidgetBox(min_date, max_date) # filter_select, daytime_select)
    layout = row(controls, plot)
    tab = Panel(child=layout, title='Filtering', width=1024)
    
    return src.data, tab
