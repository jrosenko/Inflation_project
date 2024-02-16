# dependencies
import numpy as np
import pandas as pd

from fredapi import Fred

# get data
# you need to imput your own api key
fredkey = 'xxxx'
fred = Fred(api_key=fredkey)

# create dataframe of inflation data series
df= {}

df['cpi'] = fred.get_series('CPIAUCNS')  #CPI All items index   Index 1982-1984=100, Not Seasonally Adjusted
df['cpi_goods'] = fred.get_series('CUUR0000SACL1E')  #CPI Commodities Less Food and Energy Commodities
df['cpi_services'] = fred.get_series('CUUR0000SASLE') #CPI Services Less Energy Services in U.S. City Average
df['retail_sales'] = fred.get_series('RSAFS') # Advance Retail Sales: Retail Trade and Food Services
df['avg_hourly_earnings'] = fred.get_series('CES0500000003') # A Average Hourly Earnings of All Employees, Total Private
df['ECI'] = fred.get_series('CIS1020000000000I') #Employment Cost Index: Wages and salaries for All Civilian workers in All industries and occupations
df['PCE_core'] = fred.get_series('PCEPILFE') #PCE core index values seasonally adjusted
df = pd.DataFrame(df)

# save to file for use downsteam
df.to_csv('cpi_index.csv')
