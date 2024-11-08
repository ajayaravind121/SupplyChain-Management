# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 01:12:31 2023

@author: Ryze
"""

import pandas as pd

pallet = pd.read_csv(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv"); 
pallet.info()

pallet.describe()


pallet.QTY.mean() # '.' is used to refer to the variables within object
pallet.QTY.median()
pallet.QTY.mode()

# Measures of Dispersion / Second moment business decision
pallet.QTY.var() # variance
pallet.QTY.std() # standard deviation
range = max(pallet.QTY) - min(pallet.QTY) # range
range


# Third moment business decision
pallet.QTY.skew()
pallet.QTY.skew()


# Fourth moment business decision
pallet.QTY.kurt()
pallet

