from gensim import corpora, matutils, models, similarities
from math import radians, sin, cos, sqrt, asin
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from time import sleep
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
import IPython
import pickle
import sys
import os

ip = IPython.core.getipython.get_ipython()

def warn(*args, **kwargs):
        pass
warnings.warn = warn

# Style settings
#plt.style.available 
plt.style.use('ggplot')
sns.set_context("talk")

# Option settings
#pd.describe_option('display') 
pd.options.display.max_rows = 20
pd.options.display.max_columns = 99
pd.options.display.max_colwidth = 999

# Formatting settings
float_formatter = lambda x: "%.7f" % x if x>0 else "%.7f" % x
np.set_printoptions(formatter={'float_kind':float_formatter})
pd.set_option('display.float_format', float_formatter)
ip.display_formatter.formatters['text/latex'].enabled = False
