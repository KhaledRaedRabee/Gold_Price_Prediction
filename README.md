# Gold Price Prediction

This project predicts gold prices (GLD) based on financial indicators like S&P 500, Crude Oil ETF, Silver ETF, and the EUR/USD exchange rate.

# Dataset Description:

SPX: The closing values of the S&P 500 index, a broad measure of the U.S. stock market's performance.

GLD: The closing values of the SPDR Gold Shares ETF (GLD), which tracks the price of gold.

USO: The closing values of the United States Oil Fund (USO), an exchange-traded fund that tracks the price of crude oil.

SLV: The closing values of the iShares Silver Trust (SLV), an exchange-traded fund that tracks the price of silver.

EUR/USD: The exchange rate between the Euro (EUR) and the U.S. Dollar (USD), representing the relative value of the Euro against the U.S. Dollar.

DATE: The date for which the data is recorded.

## Features

- **Data Preprocessing**: Feature engineering, scaling.
- **Machine Learning Model**: Linear (91% R² score).
- **Streamlit App**: User-friendly interface for predictions.

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-link>
   cd Gold_Price_Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Streamlit App

```bash
streamlit run gold_price_app.py
```

##

