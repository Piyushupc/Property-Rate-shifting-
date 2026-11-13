# Real Estate Price Analysis and Visualization

A desktop application for exploring Indian real-estate price patterns, comparing pre- and post-pandemic periods, and experimenting with regression-based analysis.

## Features

- Load a CSV dataset.
- Filter and explore records by city.
- Visualize data with line, bar, histogram, scatter, pie, and heatmap charts.
- Run linear regression for a continuous price target.
- Create a high/low price category for classification experiments.
- Display visualizations through a Tkinter interface.

## Technology stack

- Python
- Pandas and NumPy
- scikit-learn
- Matplotlib and Seaborn
- Tkinter

## Project structure

```text
GUI.py
Graph.py
Main.py
real_estate_pricing_pattern_india.csv
README.md
```

## Run locally

Install the dependencies:

```bash
python -m pip install pandas numpy scikit-learn matplotlib seaborn
```

Run the application:

```bash
python GUI.py
```

Keep the CSV dataset in the expected project location, or update the data-loading path if you move it.

## Modeling notes

- Linear regression is used for predicting a continuous property-price-per-square-foot target.
- Logistic regression is used for a separate high/low price classification task derived from the median price.
- The dataset's provenance, collection period, coverage, and licensing should be checked before drawing market conclusions.
- A model trained on historical observations does not automatically provide reliable future property valuations.

## Improvements to prioritize

1. Split training and test data before fitting imputers, encoders, or scalers.
2. Use a scikit-learn Pipeline and ColumnTransformer to prevent preprocessing leakage and keep inference consistent.
3. Use a time-based holdout if the goal is forecasting future prices.
4. Compare against simple baselines and report MAE, RMSE, and R² for regression.
5. Report precision, recall, F1, and ROC-AUC for classification.
6. Document the dataset source and add reproducible environment/dependency files.
7. Separate data preparation, model training, and GUI code into maintainable modules.

## Author

Piyush Rai — [GitHub](https://github.com/Piyushupc)
