import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("House-Price.csv")  

# Display first 5 rows
print("First 5 Rows of Dataset:\n")
print(df.head())

# Display column names
print("\nColumns in Dataset:")
print(df.columns)

# -----------------------------
# Select Feature and Target
# -----------------------------
# Simple Linear Regression
X = df[['sqft_living']]
y = df['price']

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Create and Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Model Evaluation
# -----------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.4f}")

# -----------------------------
# Model Parameters
# -----------------------------
print("\n========== MODEL PARAMETERS ==========")
print(f"Coefficient (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# -----------------------------
# Plot Regression Line
# -----------------------------
plt.figure(figsize=(8, 6))

plt.scatter(
    X_test,
    y_test,
    color="blue",
    label="Actual Prices"
)

plt.plot(
    X_test,
    y_pred,
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.title("House Price Prediction using Linear Regression")
plt.xlabel("Living Area (sqft)")
plt.ylabel("House Price")
plt.legend()

plt.savefig("regression_plot.png")
plt.show()

# -----------------------------
# Interpretation
# -----------------------------
print("\n========== INTERPRETATION ==========")
print(f"Every additional square foot increases the predicted house price by approximately ${model.coef_[0]:.2f}.")
print(f"The model explains approximately {r2 * 100:.2f}% of the variance in house prices.")