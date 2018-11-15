import pandas as pd
import numpy as np
import os
cwd = os.getcwd()

### Read in and set data
fundms = pd.read_csv(os.path.join(cwd, 'Data/fundamentals.csv'))
pr_split = pd.read_csv(os.path.join(cwd, 'Data/prices-split-adjusted.csv'))
prices = pd.read_csv(os.path.join(cwd, 'Data/prices.csv'))
secu = pd.read_csv(os.path.join(cwd, 'Data/securities.csv'))
