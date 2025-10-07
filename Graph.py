import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("real_estate_pricing_pattern_india.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# 1. Line Plot (Square_Feet vs Price)
plt.figure(figsize=(8,5))
plt.plot(df["Square_Feet"], df["Price_Per_SqFt"], color="blue")
plt.xlabel("Square Feet")
plt.ylabel("Price per SqFt")
plt.title("Line Graph: Square_Feet vs Price")
plt.show()

# 2. Column Graph (Avg price by City)
plt.figure(figsize=(10,6))
df.groupby("City")["Price_Per_SqFt"].mean().sort_values().plot(kind="bar", color="green")
plt.title("Average Price per SqFt by City")
plt.ylabel("Price per SqFt")
plt.show()

# 3. Histogram (Price Distribution)
plt.figure(figsize=(8,5))
plt.hist(df["Price_Per_SqFt"], bins=30, color="purple", edgecolor="black")
plt.title("Histogram: Price per SqFt Distribution")
plt.xlabel("Price per SqFt")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Square_Feet vs Price)
plt.figure(figsize=(8,5))
plt.scatter(df["Square_Feet"], df["Price_Per_SqFt"], alpha=0.5, color="red")
plt.title("Scatter Plot: Square_Feet vs Price")
plt.xlabel("Square Feet")
plt.ylabel("Price per SqFt")
plt.show()

# 5. Pie Chart (Property distribution by City)
plt.figure(figsize=(7,7))
df["City"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90, cmap="tab20")
plt.title("Pie Chart: Property Listings by City")
plt.ylabel("")
plt.show()

# 6. Heatmap (Correlation)
plt.figure(figsize=(10,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap: Feature Correlation")
plt.show()

def plot_avg_price_by_city(df):
    """Plot average price per SqFt by city"""
    df.groupby("City")["Price_Per_SqFt"].mean().sort_values().plot(kind="bar", color="green")
    plt.title("Average Price per SqFt by City")
    plt.ylabel("Price per SqFt")
    plt.show()
