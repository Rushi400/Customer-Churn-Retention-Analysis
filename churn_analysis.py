import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Telco-Customer-Churn.csv")

# Clean data
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')

df.fillna(0, inplace=True)

# Feature engineering
df['Tenure_Group'] = pd.cut(
    df['tenure'],
    bins=[0, 6, 12, 24, df['tenure'].max()],
    labels=['0-6', '6-12', '12-24', '24+'],
    include_lowest=True
)

df['CLV'] = df['MonthlyCharges'] * df['tenure']

# Analysis
print("Churn %:")
print(df['Churn'].value_counts(normalize=True) * 100)

print("\nChurn by Tenure:")
print(df.groupby('Tenure_Group')['Churn'].value_counts(normalize=True))

print("\nChurn by Contract:")
print(df.groupby('Contract')['Churn'].value_counts())

# Export for Power BI
df.to_csv("churn_final.csv", index=False)
print("Exported churn_final.csv")
