import pandas as pd 
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 50)
pd.set_option('display.max_rows', 500)

survey_file_input = "survey.csv" 
raw_df = pd.read_csv(survey_file_input)
print(raw_df)
t_data = raw_df [["Age", "Gender", "Country", "state","anonymity","self_employed", "coworkers","remote_work", "tech_company","family_history", "treatment", "mental_health_consequence","phys_health_consequence"]]
print (t_data)


t_data.loc[(t_data['anonymity']).isin((['Yes', "Don't know"])), "anonymity"] = "Yes"
t_data.loc[(t_data['coworkers'].isin(['Yes', 'Some of them'])), "coworkers"] = "Yes"

Lgenders_female = ["female", "Cis Female", "F", "Woman", "4"] 
Lgenders_male = ["W", "male", "e", "Male-ish", "maile", "Cis Male", "Mal", "Male (CIS)"]
Lgenders_nonbinary = ["Trans-female", "something kinda male?", "queer/she/they 'non-binary"]


t_data.loc[(t_data['Gender'].isin(Lgenders_female)), "Gender"] = "Female"
t_data.loc[(t_data['Gender'].isin(Lgenders_male)), "Gender"] = "male"
t_data.loc[(t_data['Gender'].isin(Lgenders_nonbinary)), "Gender"] = "nonbinary"

print(t_data['Gender'].unique())





