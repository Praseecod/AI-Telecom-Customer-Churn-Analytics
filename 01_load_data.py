import pandas as pd
import numpy as np
df = pd.read_csv(r"C:/Users/murug/Downloads/archive (2)/synthetic_customer_churn_100k.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df['CustomerID'].duplicated().sum())
print(df['Gender'].unique())
print(df['Contract'].unique())
print(df['PaymentMethod'].unique())
print(df['Churn'].unique())
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True) * 100)
print(df[['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges']].describe())
print((df['TotalCharges'] < 0).sum())
print(df[df['TotalCharges'] < 0])
negative = df[df['TotalCharges'] < 0]
print(negative[['Tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']].describe())
print(negative[['Tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']].head(10))
df['ExpectedCharges'] = df['Tenure'] * df['MonthlyCharges']
print(df[['Tenure', 'MonthlyCharges', 'TotalCharges', 'ExpectedCharges']].head())
df = df.drop('ExpectedCharges', axis=1)
print(df.columns)
import numpy as np
df.loc[df['TotalCharges'] < 0, 'TotalCharges'] = np.nan
print(df['TotalCharges'].isnull().sum())
df['TotalCharges'] = df['TotalCharges'].fillna(
    df['Tenure'] * df['MonthlyCharges']
)
