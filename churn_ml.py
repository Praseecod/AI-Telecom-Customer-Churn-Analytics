import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:/Users/murug/Downloads/archive (2)/synthetic_customer_churn_100k.csv")

# Convert Churn into numbers
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# Convert categorical columns into dummy variables
df_ml = pd.get_dummies(
    df,
    columns=["Gender", "Contract", "PaymentMethod"],
    drop_first=True
)

# Separate features and target
X = df_ml.drop(["CustomerID", "Churn"], axis=1)
y = df_ml["Churn"]

print("Features:")
print(X.columns)

print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)
from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
from sklearn.linear_model import LogisticRegression

# Create the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

print("Logistic Regression model trained successfully!")
# Make predictions on the test data
y_pred = model.predict(X_test)

print("Predictions completed successfully!")
print("First 10 predictions:", y_pred[:10])
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Logistic Regression Accuracy:", accuracy)

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
from sklearn.ensemble import RandomForestClassifier

# Create Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
rf_model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully!")
# Make predictions using Random Forest
rf_pred = rf_model.predict(X_test)

print("\nRandom Forest predictions completed!")
print("First 10 predictions:", rf_pred[:10])
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Calculate Random Forest accuracy
rf_accuracy = accuracy_score(y_test, rf_pred)

print("\nRandom Forest Accuracy:", rf_accuracy)

# Detailed classification report
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_pred))

# Confusion Matrix
print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_pred))
# Get feature importance from Random Forest
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

# Sort from highest to lowest
feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)
import matplotlib.pyplot as plt

# Create feature importance chart
plt.figure(figsize=(10, 6))

plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance")

plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig("feature_importance.png")
plt.show()
