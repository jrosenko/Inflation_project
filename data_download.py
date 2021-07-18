# dependencies
import numpy as np
import pandas as pd

from fredapi import Fred

# get data
# you need to imput your own api key
fred = Fred(api_key='XXXX')
cpi = fred.get_series('CPIAUCSL')

cpi.to_csv('cpi_index.csv')
