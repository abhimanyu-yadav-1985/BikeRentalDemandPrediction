# %%
import pandas as pd
import numpy as np

import sweetviz as sv

import os
#%%
raw_data_path = os.path.join(os.getcwd(), '.data', 'raw_data.csv')
df = pd.read_csv(raw_data_path, low_memory=False, compression='gzip')

print(f'Number of Records in Raw DataFrame: {len(df)}')

#%%
# - Business Data cleaning step 1
# A single customer id can only have a single entry at a given timestamp

# check how many such entries exist
print(f"Number of duplicated entries: {len(df[df.duplicated(subset=['ts','number'], keep=False)])}")

#%%
# - Drop the duplicated entries

df.drop_duplicates(subset=['ts', 'number'], inplace=True, keep='last')
df.reset_index(inplace=True, drop=True)

print(f"Number of Records in DataFrame after clean 1: {len(df)}")

# %%
# - Check for missing values

df.isnull().sum()
# There are no missing values

# %%
# - The customer id is object and non numeric we need to convert it to numeric type

df['number'] = pd.to_numeric(df['number'], errors='coerce')

# now count zero values again
df.isnull().sum()

# Drop any null customer id : This can be because of any number of problems
df.dropna(inplace=True)

df.isnull().sum()

print(f"Number of Records in DataFrame after clean 2: {len(df)}")
# %%
df.head()
# %%
# Convert the format of column ts to timestamp

df['ts'] = pd.to_datetime(df['ts'])

df.head()
df.info()

# %%
# Now we need to create extra features by changing the timestamp to hours, mins, day, month, year, dayofweek

df['hour'] = df['ts'].dt.hour
df['min'] = df['ts'].dt.minute
df['day'] = df['ts'].dt.day
df['month'] = df['ts'].dt.month
df['year'] = df['ts'].dt.year
df['dayofweek'] = df['ts'].dt.dayofweek

df.head()

# %%
