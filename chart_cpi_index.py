import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('cpi_index.csv')

# change name of date column and make datetime object
df.rename(columns={'Unnamed: 0' : 'Date'}, inplace = True)
df['Date'] = pd.to_datetime(df.Date)

# create chart data frame
chart_df = df[df.Date > '2016']

# chart index from 2016 to present
fig = plt.figure(figsize=(8, 6))
plt.plot(chart_df.Date, chart_df.cpi)
plt.title('CPI Index')
plt.show()