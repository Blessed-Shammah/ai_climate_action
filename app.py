import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load dataset (e.g., World Bank CO2 emissions and related features)
# For demo, assume a CSV with columns: year, gdp, population, energy_use, co2_emissions
url = "https://raw.githubusercontent.com/datasets/co2-emissions/master/data/co2_emissions.csv"
data = pd.read_csv(url)

# Preprocess data
data = data.dropna()  # Remove missing values
features = ['gdp', 'population', 'energy_use']  # Example features
X = data[features]
y = data['co2_emissions']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Visualize results
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual CO2 Emissions')
plt.ylabel('Predicted CO2 Emissions')
plt.title('CO2 Emissions Prediction')
plt.savefig('co2_prediction_plot.png')
plt.show()