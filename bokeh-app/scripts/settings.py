STATIONS = { 'HSL' :
             {
             'DATA_BUCKET' : 'usgs-hsl-backup'
             'DATA_DIRECTORY' : '/home/ubuntu/ec-data/'
             },
             'YLT' :
             {
             'DATA_BUCKET' : 'usgs-ylt-backup'
             'DATA_DIRECTORY' : '/home/ubuntu/ec-data-yellowstone/'
             }
           }

CO2_FLUX_TOOLTIPS = [('Date', '@Date{%F}'),
                     ('CO2 flux', '$@{co2_flux}{%.2f}')
                    ]
