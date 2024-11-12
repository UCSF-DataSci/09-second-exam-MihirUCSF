import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy import stats

# Load the cleaned data
data = pd.read_csv('C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv')
data['visit_date'] = pd.to_datetime(data['visit_date'])

# Handle missing data
data = data.dropna()

# Analyze walking speed
# Multiple regression with education and age
model_walking_speed = smf.ols('walking_speed ~ education_level + age', data=data).fit()
print(model_walking_speed.summary())

# Account for repeated measures
model_mixed = smf.mixedlm('walking_speed ~ education_level + age', data, groups=data['patient_id']).fit()
print(model_mixed.summary())

# Test for significant trends
anova_results = sm.stats.anova_lm(model_walking_speed, typ=2)
print("\nANOVA results for walking speed model:")
print(anova_results)

# Analyze costs
# Simple analysis of insurance type effect
model_costs = smf.ols('visit_cost ~ insurance_type', data=data).fit()
print(model_costs.summary())

# Box plots and basic statistics
data.boxplot(column='visit_cost', by='insurance_type')
plt.title('Visit Costs by Insurance Type')
plt.suptitle('')
plt.xlabel('Insurance Type')
plt.ylabel('Visit Cost')
plt.show()

# Calculate effect sizes
effect_sizes = data.groupby('insurance_type')['visit_cost'].mean()
print("\nEffect sizes (mean visit costs by insurance type):")
print(effect_sizes)

# Advanced analysis
# Education age interaction effects on walking speed
model_interaction = smf.ols('walking_speed ~ education_level * age', data=data).fit()
print(model_interaction.summary())

# Control for relevant confounders
model_confounded = smf.ols('walking_speed ~ education_level * age + insurance_type', data=data).fit()
print(model_confounded.summary())

# Report key statistics and p-values
print("\nKey statistics and p-values for confounded model:")
print(model_confounded.summary2().tables[1][['Coef.', 'P>|t|']])