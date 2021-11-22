# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# %%
train_df = pd.read_csv('/home/lzhao/data/tmp/crypto/train.csv')
asset_details_df = pd.read_csv('/home/lzhao/data/tmp/crypto/asset_details.csv')

# %%
train_df.head(5)

# %%
asset_details_df.head(5)

# %%
print(train_df['timestamp'].min())
print(train_df['timestamp'].max())


# %%
print(train_df.shape)
# %%
test = train_df[train_df.Asset_ID == 1]
# %%
test.shape
# %%
train_df['timestamp'] = train_df['timestamp'].astype('datetime64[s]')

# %%
test = train_df[train_df.Asset_ID == 1]
test[['timestamp','Count']].resample('D', on='timestamp').sum().shape
# %%
from time_series_split import PurgedGroupTimeSeriesSplit
