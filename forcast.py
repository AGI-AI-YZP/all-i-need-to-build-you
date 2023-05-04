import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

# Function to test stationarity
def test_stationarity(timeseries):
    result = adfuller(timeseries)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])

# Load your time series data
data = {
    'date': pd.date_range('2022-01-01', '2022-01-31', freq='D'),
    'value': np.random.randint(10, 50, size=31)
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Decompose the time series to visualize trend and seasonality
decomposition = seasonal_decompose(df)
fig = decomposition.plot()
plt.show()

# Check stationarity
test_stationarity(df['value'])

# Difference the time series to make it stationary
diff = df['value'].diff().dropna()

# Re-check stationarity
test_stationarity(diff)

# Grid search for the best SARIMAX model parameters
p = q = range(0, 3)
d = range(0, 2)
pdq = list(itertools.product(p, d, q))

best_aic = np.inf
best_pdq = None
best_model = None

for param in pdq:
    try:
        model = SARIMAX(df, order=param)
        results = model.fit()
        
        if results.aic < best_aic:
            best_aic = results.aic
            best_pdq = param
            best_model = results
    except:
        continue

print(f"Best model: SARIMAX{best_pdq} with AIC {best_aic}")

# Model diagnostics
best_model.plot_diagnostics(figsize=(15, 12))
plt.show()

# Make future predictions
forecast = best_model.get_forecast(steps=5)  # Predict the next 5 days
forecast_ci = forecast.conf_int()

# Display the predictions
print(forecast.predicted_mean)
print(forecast_ci)