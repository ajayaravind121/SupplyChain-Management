# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:51:20 2023

@author: Ryze
"""
import numpy as np
import pandas as pd
import seaborn as sns


pallet = pd.read_csv(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv"); 
pallet.info()

pallet.describe()

pallet.count()

#First moment business decision
pallet[pallet['Transaction Type'] == 'Allot']['QTY'].mean()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].mean()

pallet[pallet['Transaction Type'] == 'Allot']['QTY'].median()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].median()

pallet[pallet['Transaction Type'] == 'Allot']['QTY'].mode()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].mode()


#Second moment business decision
pallet[pallet['Transaction Type'] == 'Allot']['QTY'].var()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].var()

pallet[pallet['Transaction Type'] == 'Allot']['QTY'].std()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].std()

Allotrange = max(pallet[pallet['Transaction Type'] == 'Allot']['QTY']) - min(pallet[pallet['Transaction Type'] == 'Allot']['QTY']) 
Allotrange
returnrange = max(pallet[pallet['Transaction Type'] == 'Return']['QTY']) - min(pallet[pallet['Transaction Type'] == 'Return']['QTY']) 

# Third moment business decision
pallet[pallet['Transaction Type'] == 'Allot']['QTY'].skew()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].skew()

# Fourth moment business decision
pallet[pallet['Transaction Type'] == 'Allot']['QTY'].kurt()
pallet[pallet['Transaction Type'] == 'Return']['QTY'].kurt()

pallet
#transformation
data = pallet.drop("S.NO",axis=1)
#rename column
data = data.rename(columns={'Transaction Type': 'transactiontype'})

#handling duplicates
data.drop_duplicates(inplace=True)
print(data.shape)


#negative to positive
data['QTY'] = np.where(data['QTY'] < 0, -data['QTY'], data['QTY'])
data
sns.boxplot(data.qty, x=data.transactiontype == "Return")
sns.boxplot(data.qty, x=data.transactiontype == "Allot")

#First moment business decision
data[data['Transaction Type'] == 'Allot']['QTY'].mean()
data[data['Transaction Type'] == 'Return']['QTY'].mean()

data[data['Transaction Type'] == 'Allot']['QTY'].median()
data[data['Transaction Type'] == 'Return']['QTY'].median()

data[data['Transaction Type'] == 'Allot']['QTY'].mode()
data[data['Transaction Type'] == 'Return']['QTY'].mode()


#Second moment business decision
data[data['Transaction Type'] == 'Allot']['QTY'].var()
data[data['Transaction Type'] == 'Return']['QTY'].var()

data[data['Transaction Type'] == 'Allot']['QTY'].std()
data[data['Transaction Type'] == 'Return']['QTY'].std()

Allotrange = max(data[data['Transaction Type'] == 'Allot']['QTY']) - min(data[data['Transaction Type'] == 'Allot']['QTY']) 
Allotrange
returnrange = max(data[data['Transaction Type'] == 'Return']['QTY']) - min(data[data['Transaction Type'] == 'Return']['QTY']) 
returnrange
# Third moment business decision
data[data['Transaction Type'] == 'Allot']['QTY'].skew()
data[data['Transaction Type'] == 'Return']['QTY'].skew()

# Fourth moment business decision
data[data['Transaction Type'] == 'Allot']['QTY'].kurt()
data[data['Transaction Type'] == 'Return']['QTY'].kurt()

import scipy.stats as stats
import pylab
stats.probplot(data.qty, dist = "norm", plot = pylab)

# For MySQL
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:3690@127.0.0.1:3306/project')
# Use pandas to write the dataframe to the database
data.to_sql('new_pallet', con=engine, if_exists='replace', index=False)

