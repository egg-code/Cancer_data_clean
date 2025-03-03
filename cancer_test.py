from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session, DeclarativeBase
from base import Base, Patient, Cancer, Confidential
from cancer_clean import patient_df, cancer_df, confidential_df
import pandas as pd

#Connect to sqlite database
engine = create_engine("sqlite:///cancer.db")
conn = engine.connect()
Base.metadata.create_all(engine) # Create tables from base.py

# Insert data into sqlite tables if they exist

with Session(engine) as session:
    for _, row in patient_df.iterrows():
        existing_patient = session.query(Patient).filter(Patient.Patient_ID == row['Patient_ID']).first()
        if not existing_patient:
            patient = Patient(
                Patient_ID=row['Patient_ID'],
                Country=row['Country'],
                Age=row['Age'],
                Gender=row['Gender'],
                Family_History=row['Family_History'],
                Smoking_History=row['Smoking_History'],
                Alcohol_Consumption=row['Alcohol_Consumption']
            )
            session.add(patient)
    
    for _, row in cancer_df.iterrows():
        existing_cancer = session.query(Cancer).filter(Cancer.Patient_ID == row['Patient_ID']).first()
        if not existing_cancer:
            cancer = Cancer(
                Patient_ID=row['Patient_ID'],
                Cancer_Stage=row['Cancer_Stage'],
                Tumor_Size_mm=row['Tumor_Size_mm'],
                Early_Detection=row['Early_Detection'],
                Treatment_Type=row['Treatment_Type']
            )
            session.add(cancer)

    for _, row in confidential_df.iterrows():
        existing_confidential = session.query(Confidential).filter(Confidential.Patient_ID == row['Patient_ID']).first()
        if not existing_confidential:
            confidential = Confidential(
                Patient_ID=row['Patient_ID'],
                Genetic_Mutation=row['Genetic_Mutation'],
                Survival_5_years=row['Survival_5_years'],
                Mortality=row['Mortality'],
                Economic_Classification=row['Economic_Classification'],
                Healthcare_Access=row['Healthcare_Access'],
                Survival_Prediction=row['Survival_Prediction']
            )
            session.add(confidential)
    session.commit()

#Read data from tables using ORM limit to 10 rows
"""with Session(engine) as session:
    query_p = session.query(Patient).limit(10)
    query_c = session.query(Cancer).limit(10)
    query_cf = session.query(Confidential).limit(10)
    
    for row in query_p: #Patient table
        print(row)
    
    for row in query_c: #Cancer table
        print(row)

    for row in query_cf: #Confidential table
        print(row)"""

#Read data from tables using SQL statement limit to 10 rows
with Session(engine) as session:
    
    #Querying Patient table
    query_p = session.execute(text("SELECT * FROM patient LIMIT 10"))
    patientsql_df = pd.DataFrame(query_p.fetchall(), columns=query_p.keys())

    #Querying Cancer table
    query_c = session.execute(text("SELECT * FROM cancer LIMIT 10"))
    cancersql_df = pd.DataFrame(query_c.fetchall(), columns=query_c.keys())

    #Querying Confidential table
    query_cf = session.execute(text("SELECT * FROM confidential LIMIT 10"))
    confidentialsql_df = pd.DataFrame(query_cf.fetchall(), columns=query_cf.keys())
    
    print(patientsql_df)
    print(cancersql_df)
    print(confidentialsql_df)

#Close the connection
conn.close()
engine.dispose()

