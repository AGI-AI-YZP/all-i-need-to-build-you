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

# Function to train the SARIMAX model
def train_sarimax_model(df):
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
    
    return best_model

# Function to forecast new data points
def forecast_new_data(new_data, trained_model, steps=5):
    updated_df = df.append(new_data)
    updated_model = SARIMAX(updated_df, order=trained_model.model_orders)
    updated_results = updated_model.smooth(trained_model.params)
    forecast = updated_results.get_forecast(steps=steps)
    forecast_ci = forecast.conf_int()
    
    return forecast.predicted_mean, forecast_ci

# Load your time series data
data = {
    'date': pd.date_range('2022-01-01', '2022-01-31', freq='D'),
    'value': np.random.randint(10, 50, size=31)
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Train the SARIMAX model
trained_model = train_sarimax_model(df)

# New data points
new_data = pd.DataFrame({'value': np.random.randint(10, 50, size=5)}, index=pd.date_range('2022-02-01', '2022-02-05', freq='D'))

# Forecast with the new data points
forecast, forecast_ci = forecast_new_data(new_data, trained_model, steps=5)

# Display the predictions
print(forecast)
print(forecast_ci)