# Load the Data
import pandas as pd
df = pd.read_csv(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv"); 
#transformation
df = df.drop("S.NO",axis=1)

# Auto EDA
# Sweetviz
# Dtale
# Pandas Profiling
# Dataprep
#Autoviz



# Sweetviz
###########
#pip install sweetviz
import sweetviz as sv
s = sv.analyze(df)
s.show_html()

import os
os.getcwd()

# Autoviz
###########
# pip install autoviz
from autoviz.AutoViz_Class import AutoViz_Class
av = AutoViz_Class()
a = av.AutoViz(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv", chart_format = 'html')

import os
os.getcwd()


# D-Tale
########

#pip install dtale 
  # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
import dtale
import pandas as pd

df = pd.read_csv(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv")
#transformation
df = df.drop("S.NO",axis=1)
d = dtale.show(df)
d.open_browser()


# Pandas Profiling
###################

#pip install pandas_profiling
import pandas as pd
from pandas_profiling import ProfileReport 
df = pd.read_csv(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv")
#transformation
df = df.drop("S.NO",axis=1)
p = ProfileReport(df)
p
p.to_file("output.html")

import os
os.getcwd()

# Dataprep
##########
#pip install werkzeug==2.3
#pip install dataprep
from dataprep.eda import create_report
import pandas as pd
df = pd.read_csv(r"C:\Users\Ryze\OneDrive\Desktop\Projects\Innodatatics\dataproprocessing\pallet_Masked_fulldata.csv")
#transformation
df = df.drop("S.NO",axis=1)
report = create_report(df, title = 'My Report')

report.show_browser()


