import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, roc_auc_score

# Change directory if necessary
os.chdir(r'D:\Desktop\vscode\projects\python\aspirenex\prediction churn model')

# Load the data
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Display column names to verify 'Churn' column
print(df.columns)

# Convert 'TotalCharges' to numeric, coerce errors, and handle missing values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# Check 'Churn' column values and convert to numeric if necessary
print(df['Churn'].unique())
if df['Churn'].dtype == 'object':
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Verify the conversion
print(df['Churn'].unique())

# Data cleaning and preprocessing
df = pd.get_dummies(df, drop_first=True)

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('Churn', axis=1))

# Split the data
X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['Churn'], test_size=0.2, random_state=42)

# Train models
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier()
}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"{name}:\n {classification_report(y_test, predictions)}\n")
    print(f"ROC-AUC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1])}\n")
