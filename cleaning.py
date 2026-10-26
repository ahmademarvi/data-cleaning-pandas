
import pandas as pd

def clean_shark_data(df):
    # Create a copy
    data = df.copy()

    # Remove unnecessary columns
    data = data.drop(
        columns=["Unnamed: 21", "Unnamed: 22"],
        errors="ignore"
    )

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Handle missing values
    for col in ["Country", "Activity", "Sex"]:
        data[col] = data[col].fillna("Unknown")

    # Clean country names
    data["Country"] = data["Country"].str.strip().str.title()

    data["Country"] = data["Country"].replace({
        "Usa": "USA",
        "United States": "USA",
        "U.S.A.": "USA"
    })

    # Clean activity names
    data["Activity"] = data["Activity"].str.strip().str.title()

    # Clean sex values
    data["Sex"] = data["Sex"].str.strip().str.upper()

    # Convert age to numeric
    data["Age_Clean"] = pd.to_numeric(
        data["Age"], errors="coerce"
    )

    # Convert year to numeric
    data["Year"] = pd.to_numeric(
        data["Year"], errors="coerce"
    )

    return data
