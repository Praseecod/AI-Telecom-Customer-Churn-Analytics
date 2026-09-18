import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:/Users/murug/Downloads/archive (2)/synthetic_customer_churn_100k.csv")

# Create ChargeGroup
df['ChargeGroup'] = pd.cut(
    df['MonthlyCharges'],
    bins=[0, 50, 75, 100, float('inf')],
    labels=['Low', 'Medium', 'High', 'Very High']
)

# Calculate churn percentage
chargegroup_churn = pd.crosstab(
    df['ChargeGroup'],
    df['Churn'],
    normalize='index'
) * 100

# Create bar chart
chargegroup_churn['Yes'].plot(kind='bar')

plt.title('Churn Rate by Charge Group')
plt.xlabel('Charge Group')
plt.ylabel('Churn Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig('chargegroup_churn.png')
plt.show()
