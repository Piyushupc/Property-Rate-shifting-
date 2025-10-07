import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
from sklearn.impute import SimpleImputer

# Load dataset
try:
    df = pd.read_csv("real_estate_pricing_pattern_india.csv")
except FileNotFoundError:
    print("Dataset not found. Please ensure 'real_estate_pricing_pattern_india.csv' is in the working directory.")
    exit()

# Drop useless unnamed columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# =============================
# 1. Linear Regression
# =============================
print("\n=== Linear Regression: Predict Property Price 2025 ===")
lin_data = df.dropna(subset=["Price_Per_SqFt"])

X = lin_data.drop(columns=["Price_Per_SqFt"])
X = pd.get_dummies(X, drop_first=True)   # Encode categorical
y = lin_data["Price_Per_SqFt"]

# Handle missing values with imputer
imputer = SimpleImputer(strategy="mean")
X_imputed = imputer.fit_transform(X)
X = pd.DataFrame(X_imputed, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

y_pred = lin_model.predict(X_test)

print("Linear Regression Results:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))


# =============================
# 2. Logistic Regression
# =============================
print("\n=== Logistic Regression: Classify High vs Low Property Price ===")
log_data = lin_data.copy()

# Create binary target based on median
median_price = log_data["Price_Per_SqFt"].median()
log_data["Price_Category"] = np.where(log_data["Price_Per_SqFt"] > median_price, 1, 0)

X = log_data.drop(columns=["Price_Per_SqFt", "Price_Category"])
X = pd.get_dummies(X, drop_first=True)
y = log_data["Price_Category"]

# Handle missing values
X_imputed = imputer.fit_transform(X)
X = pd.DataFrame(X_imputed, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_model = LogisticRegression(max_iter=1000, solver="liblinear")
log_model.fit(X_train, y_train)

y_pred = log_model.predict(X_test)

print("Logistic Regression Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))



# =============================
# Make functions usable by GUI
# =============================
def run_models():
    """Used by GUI to run linear regression and get metrics."""
    try:
        df = pd.read_csv("real_estate_pricing_pattern_india.csv")
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        lin_data = df.dropna(subset=["Price_Per_SqFt"])
        X = lin_data.drop(columns=["Price_Per_SqFt"])
        X = pd.get_dummies(X, drop_first=True)
        y = lin_data["Price_Per_SqFt"]

   

        imputer = SimpleImputer(strategy="mean")
        X = imputer.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression().fit(X_train, y_train)
        pred = model.predict(X_test)

        mse = mean_squared_error(y_test, pred)
        r2 = r2_score(y_test, pred)

        return {"MSE": mse, "R2": r2}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    print("Run this file directly to test regression model.")
