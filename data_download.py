# dependencies
import numpy as np
import pandas as pd

from fredapi import Fred

# get data
# you need to imput your own api key
fredkey = 'XXXX'
fred = Fred(api_key=fredkey)

# create dataframe of inflation data series
df= {}

df['cpi'] = fred.get_series('CPIAUCSL')  #CPI All items index
df['cpi_goods'] = fred.get_series('CUSR0000SACL1E')  #CPI Commodities Less Food and Energy Commodities
df['cpi_services'] = fred.get_series('CUSR0000SASLE') #CPI Services Less Energy Services in U.S. City Average

df = pd.DataFrame(df)

# save to file for use downsteam
df.to_csv('cpi_index.csv')
