# Diwali Sales Data Analysis

## Overview
This repository contains the complete code and analysis for the Diwali Sales Data Analysis project. The project aims to understand various aspects of sales performance during the Diwali season, leveraging Python for data analysis and visualization.

## Contents
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Gender-wise Sales Analysis](#gender-wise-sales-analysis)
  - [Age Group Analysis](#age-group-analysis)
  - [State-wise Sales Performance](#state-wise-sales-performance)
  - [Marital Status Impact on Sales](#marital-status-impact-on-sales)
  - [Occupation-wise Sales Analysis](#occupation-wise-sales-analysis)
  - [Product Performance Analysis](#product-performance-analysis)
- [Key Libraries Used](#key-libraries-used)
- [How to Run](#how-to-run)
- [Contact](#contact)

## Data Cleaning and Preprocessing
Below is the Python code used for data cleaning and preprocessing.

```python
# Import Python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # Visualizing data
%matplotlib inline
import seaborn as sns

# Import CSV file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Display dataset shape and preview data
print(df.shape)
print(df.head())

# Check dataset information
df.info()

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
print(pd.isnull(df).sum())

# Drop rows with null values
df.dropna(inplace=True)

# Change data type of 'Amount' column
df['Amount'] = df['Amount'].astype('int')

# Rename columns for better clarity
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Preview cleaned data
print(df.describe())
```

## Exploratory Data Analysis (EDA)

### Gender-wise Sales Analysis
- Analyzed sales distribution and total sales amount across different genders.

### Age Group Analysis
- Examined sales trends across different age groups, further segmented by gender.

### State-wise Sales Performance
- Identified top-performing states in terms of order quantity and total sales amount.

### Marital Status Impact on Sales
- Explored how marital status affects sales, with a breakdown by gender.

### Occupation-wise Sales Analysis
- Assessed sales performance across different occupations.

### Product Performance Analysis
- Determined the top 10 products based on order quantity.

## Key Libraries Used
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

## How to Run
1. Clone the repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the provided code in a Jupyter Notebook or Python IDE to analyze the data and visualize the insights.

## Contact
For further questions or collaboration opportunities, feel free to reach out to me:
- **GitHub:** [MinaJoseph01](https://github.com/MinaJoseph01)
- **LinkedIn:** [Mina Joseph](https://www.linkedin.com/in/minajosephamir/)
