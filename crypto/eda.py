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


