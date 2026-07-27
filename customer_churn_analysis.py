import pandas as pd

# 1. Load the raw dataset
file_path = r"C:\Users\i0240\OneDrive\Desktop\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

print("--- Initial Data Info ---")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}\n")

# 2. Fix the "TotalCharges" hidden space bug
# Convert spaces to NaN (Not a Number), then convert the whole column to numeric floats
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check how many missing values we just exposed
missing_charges = df['TotalCharges'].isnull().sum()
print(f"Missing values found in TotalCharges: {missing_charges}")

# 3. Drop the missing values since there are very few of them
df_clean = df.dropna(subset=['TotalCharges']).copy()

# 4. Quick look at the target variable (Churn)
print("\n--- Churn Breakdown ---")
print(df_clean['Churn'].value_counts())