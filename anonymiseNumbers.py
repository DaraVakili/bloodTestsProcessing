#%%
#import modules and files 
import pandas as pd
import os

# %%
df = pd.read_csv(
    '../data/data1Table1.txt', sep='\t')


df["PatientIDExternal"] = df.PatientIDExternal.astype("category").cat.codes
df["Clinician_Code"] = df.Clinician_Code.astype(
    "category").cat.codes

df.to_pickle("../data/practiceData.pickle")

# %%
