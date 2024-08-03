import pandas as pd
import numpy as np

data = pd.DataFrame({
    'A': [1, 2, np.nan],   # Column 'A' with values 1, 2, and NaN
    'B': [np.nan, 4, 5],   # Column 'B' with values NaN, 4, and 5
    'C': [6, 7, 8]         # Column 'C' with values 6, 7, and 8
})
