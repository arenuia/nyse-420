import pandas as pd
import numpy as np
from keras.layers import Input, LSTM, Dense, Dropout
from keras.models import Sequential, Model, load_model
import sys
from IPython.core.display import display, HTML
import os
cwd = os.getcwd()

### Read in and set data
fundms = pd.read_csv(os.path.join(cwd, 'Data/fundamentals.csv'))
prices_sp = pd.read_csv(os.path.join(cwd, 'Data/prices-split-adjusted.csv'))
prices = pd.read_csv(os.path.join(cwd, 'Data/prices.csv'))
secu = pd.read_csv(os.path.join(cwd, 'Data/securities.csv'))

prices.head()
