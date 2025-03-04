import pandas as pd

#Load the data
df = pd.read_csv("colorectal_cancer_dataset.csv")

patient_df = df[['Patient_ID', 'Country', 'Age', 'Gender', 'Family_History', 'Smoking_History', 'Alcohol_Consumption',]]
cancer_df = df[['Patient_ID', 'Cancer_Stage', 'Tumor_Size_mm', 'Early_Detection', 'Treatment_Type']]
confidential_df = df[['Patient_ID', 'Genetic_Mutation', 'Survival_5_years', 'Mortality', 'Economic_Classification', 'Healthcare_Access', 'Survival_Prediction']]

##Transform columns to boolean
target_columns = ['Family_History', 'Smoking_History', 'Alcohol_Consumption']
for col in target_columns:
    patient_df.loc[:, col] = patient_df[col].map({'Yes': True, 'No': False})

#Transform Cancer_Stage to ordinal and Early_Detection to boolean
cancer_df.loc[:, 'Cancer_Stage'] = cancer_df['Cancer_Stage'].map({'Localized': 1, 'Regional': 2, 'Metastatic': 3})
cancer_df.loc[:, 'Early_Detection'] = cancer_df['Early_Detection'].apply(lambda x: True if x == 'Yes' else False)

##Transform columns to boolean
columns = ['Genetic_Mutation', 'Survival_5_years', 'Mortality', 'Survival_Prediction']
for col in columns:
    confidential_df.loc[:, col] = confidential_df[col].apply(lambda x: True if x == 'Yes' else False)

##Transform Healthcare_Access to ordinal
confidential_df.loc[:, 'Healthcare_Access'] = confidential_df['Healthcare_Access'].map({'Low': 'B', 'Moderate': 'A', 'High' : 'S'})

#DFs to CSV
patient_df.to_csv('patient.csv', index=False)
cancer_df.to_csv('cancer.csv', index=False)
confidential_df.to_csv('confidential.csv', index=False)
print("Data saved to CSV files")
print(f"Patient data: {patient_df.shape}")
print(f"Cancer data: {cancer_df.shape}")
print(f"Confidential data: {confidential_df.shape}")