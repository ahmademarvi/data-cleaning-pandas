# Shark Attack Data Analysis

## Project Overview
This project analyzes historical shark attack records using Python and Pandas.

The goal is to clean the dataset, explore patterns, and test three hypotheses.

## Dataset
- Original records: 7,125
- Original columns: 23
- Source file: GSAF5.xls

## Hypotheses
1. The USA and Australia have the highest number of reported shark attacks.
2. More shark attacks are reported during surfing than swimming.
3. The number of reported shark attacks changes over time.

## Data Cleaning
The following techniques were applied:
1. Removing unnecessary columns
2. Checking and removing duplicate rows
3. Handling missing values
4. Standardizing text values
5. Converting data types

## Exploratory Data Analysis
The analysis includes:
- Top 10 countries by reported shark attacks
- Surfing vs Swimming
- Shark attacks over time (1950-2025)

## Key Findings
- USA: 2,597 reported attacks
- Australia: 1,538 reported attacks
- Surfing: 1,162 reported attacks
- Swimming: 1,075 reported attacks
- Reported attacks fluctuate considerably over time.

These results describe reported incidents, not individual shark attack risk.

## Technologies
- Python
- Pandas
- Matplotlib
- Google Colab

## Project Files
- shark_attacks_analysis.ipynb
- cleaning.py
- README.md
- GSAF5.xls

## How to Run
1. Install pandas, matplotlib and xlrd.
2. Open the notebook.
3. Load GSAF5.xls.
4. Run the notebook cells in order.
