import pandas as pd
import numpy as np
import random

# Load and structure the data
data = pd.read_csv('C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv')
data['visit_date'] = pd.to_datetime(data['visit_date'])
data = data.sort_values(by=['patient_id', 'visit_date'])

# Handle missing data
data = data.dropna()

# Add insurance information
insurance_types = pd.read_csv('C:/Users/mihir/OneDrive/Desktop/Assignment9/insurance.lst', header=None, names=['insurance_type'])
insurance_types = insurance_types['insurance_type'].tolist()

# Assign insurance types to each patient_id
unique_patients = data['patient_id'].unique()
patient_insurance = {patient: random.choice(insurance_types) for patient in unique_patients}
data['insurance_type'] = data['patient_id'].map(patient_insurance)

# Generate visit costs based on insurance type with random variation
def generate_cost(insurance_type):
    base_cost = {'Basic': 100, 'Premium': 200, 'Platinum': 300}
    variation = random.uniform(-20, 20)
    return base_cost[insurance_type] + variation

data['visit_cost'] = data['insurance_type'].apply(generate_cost)

# Summary statistics
# Mean walking speed by education level
mean_walking_speed_by_education = data.groupby('education_level')['walking_speed'].mean()
print("Mean walking speed by education level:")
print(mean_walking_speed_by_education)

# Mean costs by insurance type
mean_costs_by_insurance = data.groupby('insurance_type')['visit_cost'].mean()
print("\nMean costs by insurance type:")
print(mean_costs_by_insurance)

# Age effects on walking speed
age_effects_on_walking_speed = data.groupby('age')['walking_speed'].mean()
print("\nAge effects on walking speed:")
print(age_effects_on_walking_speed)