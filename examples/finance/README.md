# Financial Applications of the Hasse-Stirling Framework

This directory contains examples of applying the Hasse-Stirling computational framework to real-world financial data and problems.

## Available Examples

### 1. Option Pricing with Real Market Data

The [option_pricing_real_data.py](option_pricing_real_data.py) script demonstrates:

- Fetching real-world options data from Yahoo Finance
- Implementing both traditional and Hasse-Stirling methods for Black-Scholes option pricing
- Computing implied volatility using both approaches
- Benchmarking performance and accuracy differences
- Visualizing the results including volatility smiles and computational efficiency

### 2. Time Series Analysis of Option Pricing Methods

The [option_pricing_time_series.py](option_pricing_time_series.py) script provides:

- Analysis of both methods over multiple dates and market conditions
- Performance comparison across different volatility regimes
- Visualization of results trends over time
- Statistical analysis of method differences
- Comprehensive interpretation guidelines

## How to Compare with Longer Time Series and Interpret Results

### Running Time Series Analysis

```bash
python option_pricing_time_series.py
```

This will:
1. Generate synthetic options data across a range of dates (2020-2023)
2. Calculate implied volatilities using both methods
3. Perform statistical analysis across different market conditions
4. Create visualizations showing trends over time
5. Provide interpretation guidance in the console output

### Interpreting the Results

The script provides detailed guidance, but here are key factors to consider:

#### 1. Performance Across Market Regimes

The time series analysis segments the data into different market regimes:
- **Volatility Regimes**: Low, Medium, and High volatility periods
- **Market Trends**: Bullish vs Bearish periods

Look for patterns in method performance across these regimes. The Hasse-Stirling method often excels in high volatility environments and extreme market conditions.

#### 2. Moneyness Analysis

The analysis breaks down performance by option moneyness:
- **Deep ITM**: Options with very high moneyness (S/K > 1.15)
- **ITM**: In-the-money options (1.05 < S/K ≤ 1.15)
- **ATM**: At-the-money options (0.95 ≤ S/K ≤ 1.05)
- **OTM**: Out-of-the-money options (0.85 ≤ S/K < 0.95)
- **Deep OTM**: Options with very low moneyness (S/K < 0.85)

The Hasse-Stirling approach typically shows the greatest advantage for Deep ITM and Deep OTM options where numerical stability is most challenging.

#### 3. Key Metrics to Evaluate

When comparing methods, focus on these metrics:

- **Speedup**: Traditional computation time / Hasse-Stirling computation time
- **Error Difference**: Traditional error - Hasse-Stirling error (positive values favor Hasse-Stirling)
- **Win Ratio**: Percentage of cases where Hasse-Stirling outperforms traditional methods

#### 4. Statistical Significance

The analysis includes t-tests to determine if the differences between methods are statistically significant. A p-value < 0.05 suggests the performance difference is not due to random chance.

#### 5. Visualizations

Three key visualizations are generated:

- **time_series_performance.png**: Shows trends in performance metrics over time
- **moneyness_performance.png**: Compares performance across different moneyness categories
- **market_conditions.png**: Relates method performance to market conditions

### Extending the Analysis

To extend the analysis to your own data:

1. **Different Time Periods**: Modify the `start_date` and `end_date` parameters
2. **Different Securities**: Change the `symbol` parameter to analyze other underlyings
3. **Different Sampling Frequency**: Adjust the `interval` parameter ('1wk', '1mo', '3mo')
4. **Real vs. Synthetic Data**: The current implementation uses synthetic option data; you can modify the `fetch_options_for_date` function to use real historical options data if available

### Practical Applications

This time series analysis helps identify:

1. **When to use each method**: Based on market conditions and option characteristics
2. **Computational trade-offs**: Understanding the speed vs. accuracy balance
3. **Risk management implications**: How method choice affects valuation during market stress
4. **System design decisions**: Whether to implement a hybrid approach based on option characteristics

## Requirements

The examples require the following Python packages:

- pandas
- numpy
- matplotlib
- yfinance
- scipy

## Background: Financial Applications

The Hasse-Stirling framework provides significant advantages for financial calculations including:

1. **Options and Derivatives Pricing**: Faster and more accurate computation of prices and Greeks
2. **Risk Management**: Improved Value-at-Risk (VaR) calculations
3. **Volatility Modeling**: Better estimation of implied volatilities
4. **Fixed Income**: Enhanced yield curve construction and bond pricing

## Theoretical Basis

The Black-Scholes option pricing formula can be reformulated using hypergeometric functions:

