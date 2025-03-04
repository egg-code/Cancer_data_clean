from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

#Create a base class for the tables for cancer.db
class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ = 'patient'

    Patient_ID: Mapped[int] = mapped_column(primary_key=True)
    Country: Mapped[str] = mapped_column()
    Age: Mapped[int] = mapped_column()
    Gender: Mapped[str] = mapped_column(nullable=False)
    Family_History: Mapped[bool] = mapped_column(Boolean)
    Smoking_History: Mapped[bool] = mapped_column(Boolean)
    Alcohol_Consumption: Mapped[bool] = mapped_column(Boolean)

    cancer: Mapped['Cancer'] = relationship("Cancer", back_populates='patient')
    confidential: Mapped['Confidential'] = relationship("Confidential", back_populates='patient')

    def __repr__(self):
        return f"""Patient_ID:{self.Patient_ID}
                \nCountry:{self.Country}
                \nAge:{self.Age}
                \nGender:{self.Gender}
                \nFamily_History:{self.Family_History}
                \nSmoking_History:{self.Smoking_History}
                \nAlcohol_Consumption:{self.Alcohol_Consumption}"""

class Cancer(Base):
    __tablename__ = 'cancer'

    Patient_ID: Mapped[int] = mapped_column(ForeignKey('patient.Patient_ID'), primary_key=True)
    Cancer_Stage: Mapped[int] = mapped_column()
    Tumor_Size_mm: Mapped[int] = mapped_column()
    Early_Detection: Mapped[bool] = mapped_column(Boolean)
    Treatment_Type: Mapped[str] = mapped_column()

    patient: Mapped['Patient'] = relationship("Patient", back_populates='cancer')

    def __repr__(self):
        return f"""Patient_ID:{self.Patient_ID}
                \nCancer_Stage:{self.Cancer_Stage}
                \nTumor_Size_mm:{self.Tumor_Size_mm}
                \nEarly_Detection:{self.Early_Detection}
                \nTreatment_Type:{self.Treatment_Type}"""

class Confidential(Base):
    __tablename__ = 'confidential'
    
    Patient_ID: Mapped[int] = mapped_column(ForeignKey('patient.Patient_ID'), primary_key=True)
    Genetic_Mutation: Mapped[bool] = mapped_column(Boolean)
    Survival_5_years: Mapped[bool] = mapped_column(Boolean)
    Mortality: Mapped[bool] = mapped_column(Boolean)
    Economic_Classification: Mapped[str] = mapped_column()
    Healthcare_Access: Mapped[str] = mapped_column()
    Survival_Prediction: Mapped[bool] = mapped_column(Boolean)

    patient: Mapped['Patient'] = relationship('Patient', back_populates='confidential')

    def __repr__(self):
        return f"""Patient_ID:{self.Patient_ID}
                \nGenetic_Mutation:{self.Genetic_Mutation}
                \nSurvival_5_years:{self.Survival_5_years}
                \nMortality:{self.Mortality}
                \nEconomic_Classification:{self.Economic_Classification}
                \nHealthcare_Access:{self.Healthcare_Access}
                \nSurvival_Prediction:{self.Survival_Prediction}"""

