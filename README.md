# Real Estate Price Analysis and Visualization

A desktop application for exploring real-estate price data and comparing pre-pandemic and post-pandemic patterns. Users can load a CSV dataset, filter records by city, visualize trends, and experiment with regression models.

## Current features

- Load a user-provided CSV dataset.
- Filter and explore property records by city.
- Generate line, bar, histogram, scatter, pie, and heatmap visualizations (depending on available columns).
- Train Linear Regression for continuous price estimation.
- Train Logistic Regression for a high-price/low-price classification task.
- Explore pre-pandemic versus post-pandemic price patterns.

## Technology

Python, Tkinter, Pandas, NumPy, Matplotlib, Seaborn, and scikit-learn.

## Run locally

1. Clone the repository and create a virtual environment.
2. Install the dependencies required by the application.
3. Run `Main.py`.
4. Load a CSV file with the columns expected by the application.

Check the dataset schema and units before interpreting model results.

## Modeling notes

Linear Regression estimates a continuous property-price value. Logistic Regression is used for classification (for example, high-price versus low-price); it is not a second continuous price-prediction model.

The current preprocessing flow is an educational baseline. Fitting an imputer or other preprocessing step before the train/test split can leak test-set information into training. A robust next iteration should split first and use a scikit-learn Pipeline/ColumnTransformer so preprocessing is fitted only on training data.

## Recommended improvements

- Document dataset schema, source, currency, and time period.
- Use a reproducible train/test split and cross-validation.
- Report MAE, RMSE, and R² for regression; precision, recall, F1, and ROC-AUC where appropriate for classification.
- Compare against a simple baseline and inspect residuals.
- Add input validation, tests, and sample data licensed for redistribution.

## Author

Piyush Rai — [GitHub](https://github.com/Piyushupc)
