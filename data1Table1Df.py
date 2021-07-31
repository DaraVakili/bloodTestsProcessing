#%%
import pandas as pd
import plotly as py
from datetime import datetime, date

# %%
# year_of_birth = cleaned_df["DOB"].str[-4:].astype(int)
# year_of_birth.mean()
# changing age to years only - need a way to find exact age maybe using datetime module?

# %%
# looking aat the number of individual patients
# number_of_patients = set(cleaned_df["patientID"])
# number_of_patients.__len__()
# there are 5256 individual patients

# %%
# different_request_times = cleaned_df["requestDate"].unique()
# a variable to hold the different times tests were requested, will use to find max and min
# different_request_times.max()
# different_request_times.min()

# the function cleaned_df_function(csv_input) can be imported and used to clean the data if in the same format as data1Table1

# %%
def cleaned_df_function(csv_input):
    '''
    This function takes a .csv file 1 up from the folder it is in into the "data" folder and finally the csv itself
    it will drop clinical info, NaN data points and return a table with summary statistics
    '''
    # data from data1Table1.txt into dataframe
    df = pd.read_csv(f"../data/{csv_input}",sep='\t',header=None, error_bad_lines=False, engine='python')
    

    # changed column names
    df.columns = [
    "patientID", "DOB", "labNumber", "clinicalInfo", "requestDate", "OBXexamCodeID", "hospitalWardLocation", "resultValue", "clinicianCode"
    ]

    # df into new df without clinicalInfo
    # remove top line 
    headless_df = df.drop(df.index[[0]], axis = 0)
    # remove clinical info
    new_df = headless_df.drop(axis=1, labels="clinicalInfo")

    global cleaned_df
    # drop NaN
    cleaned_df = new_df.dropna()
    # now only look for ALT AST results
    AST_ALT_df = cleaned_df.loc[(cleaned_df['OBXexamCodeID']=='AST') | (cleaned_df['OBXexamCodeID'] == 'ALT2')]
    # remove lab, ward location and clinician code columns
    clean_AST_ALT_df = AST_ALT_df.drop(['labNumber','hospitalWardLocation','clinicianCode'],axis=1)

    return clean_AST_ALT_df

cleaned_df_function('data1Table1.txt')

# %%

# %%

# df with only AST and ALT results but is in long format
# %%
widened_AST_ALT_df = clean_AST_ALT_df.pivot(columns='OBXexamCodeID', values='resultValue', index='patientID')
widened_AST_ALT_df
# widened format doesn't work due to multiple results/patient
# %%
clean_AST_ALT_df.sort_values(by='patientID')
# %%
clean_AST_ALT_df.describe()
# there are not the same numbers of AST/ALT results - ?solution
# %%
def age(born):
    born = datetime.strptime(born, "%d/%m/%Y").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
  
clean_AST_ALT_df['Age'] = clean_AST_ALT_df['DOB'].apply(age)
  
display(clean_AST_ALT_df)
# %%
