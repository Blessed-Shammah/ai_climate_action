# AI Climate Action

A machine learning project that predicts CO2 emissions based on various economic and demographic factors using linear regression.

## Overview

This project uses machine learning to analyze and predict CO2 emissions based on several key factors:
- GDP
- Population
- Energy Usage

The model helps understand the relationship between these factors and their impact on carbon emissions, which can be valuable for climate action planning and policy-making.

## Features

- Data preprocessing and cleaning
- Linear regression model implementation
- Model performance evaluation
- Visualization of predictions vs actual values
- Uses real-world CO2 emissions data from World Bank

## Requirements

The project requires the following Python packages:
```
pandas
scikit-learn
matplotlib
numpy
```

## Installation

1. Clone the repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:
```bash
python app.py
```

The script will:
1. Load and preprocess the CO2 emissions dataset
2. Train a linear regression model
3. Make predictions on the test set
4. Display model performance metrics (MAE and R² score)
5. Generate a visualization plot saved as 'co2_prediction_plot.png'

## Model Performance

The model evaluates performance using two metrics:
- Mean Absolute Error (MAE): Measures the average magnitude of errors
- R² Score: Indicates how well the model explains the variance in the data

## Data Source

The project uses CO2 emissions data from the World Bank dataset, available at:
https://raw.githubusercontent.com/datasets/co2-emissions/master/data/co2_emissions.csv

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## License

This project is open source and available under the MIT License.
