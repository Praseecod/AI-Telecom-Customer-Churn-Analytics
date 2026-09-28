import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:/Users/murug/Downloads/archive (2)/synthetic_customer_churn_100k.csv")

# Calculate churn rate by Payment Method
payment_churn = pd.crosstab(
    df['PaymentMethod'],
    df['Churn'],
    normalize='index'
) * 100

# Create bar chart
payment_churn['Yes'].plot(kind='bar')

plt.title('Churn Rate by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Churn Rate (%)')
plt.xticks(rotation=20)
plt.tight_layout()

# Save chart
plt.savefig('paymentmethod_churn.png')
plt.show()
