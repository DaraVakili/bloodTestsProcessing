#%%
import pandas as pd

# data from data1Table1.txt into dataframe
df = pd.read_csv("../data/data1Table1.txt",sep='\t',header=None, error_bad_lines=False, engine='python')

# changed column names
df.columns = [
    "patientID", "DOB", "labNumber", "clinicalInfo", "requestDate", "OBXexamCodeID", "hospitalWardLocation", "resultValue", "clinicianCode"
]

# remove top line 
df = df.drop(df.index[[0]], axis = 0)
#%%
age = df['DOB']
print(age)

# %%
index_to_remove = df[~(df["DOB"]=='NaN')]
index_to_remove
# therefore those that need to be removed
# %%
count_nan_in_df = df.isnull().sum()
print (count_nan_in_df)

# want to drop the rows which have NaN values apart from clinical info which may not always be relevant
# will make new data drame without clinical info - keeping PTID so can refer in future
# %%
new_df = df.drop(axis=1, labels="clinicalInfo")
new_df.head()

# %%
cleaned_df = new_df.dropna()
cleaned_df
# this table should no longer have NaN - can now use for basic stats
# %%
year_of_birth = cleaned_df["DOB"].str[-4:].astype(int)
# changing age to years only - need a way to find exact age maybe using datetime module?
# %%
type(year_of_birth)
# %%
for item in year_of_birth:
    age = []
    individual_age = 2021 - item 
    age.append(individual_age)

# %%
cleaned_df.head()
# %%
number_of_patients = set(cleaned_df["patientID"])
# %%
number_of_patients.__len__()
# there are 5256 individual patients
# %%
cleaned_df["OBXexamCodeID"].value_counts()

# %%