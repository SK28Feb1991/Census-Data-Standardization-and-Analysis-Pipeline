import pandas as pd
import numpy as np


def rename_columns(df):
    """
    Renames columns for uniformity.
    """
    column_mapping = {
        'State name': 'State/UT',
        'District name': 'District',
        'Male_Literate': 'Literate_Male',
        'Female_Literate': 'Literate_Female',
        'Rural_Households': 'Households_Rural',
        'Urban_Households': 'Households_Urban',
        'Age_Group_0_29': 'Young_and_Adult',
        'Age_Group_30_49': 'Middle_Aged',
        'Age_Group_50': 'Senior_Citizen',
        'Age not stated': 'Age_Not_Stated'
    }
    df.rename(columns=column_mapping, inplace=True)
    return df


def standardize_state_names(df):
    """
    Standardizes state/UT names to title case.
    """
    df['State/UT'] = df['State/UT'].str.title().str.replace(' And ', ' and ')
    return df


def handle_new_states(df, telangana_districts, ladakh_districts):
    """
    Updates records for newly formed states/UTs.
    """
    df.loc[df['District'].isin(telangana_districts), 'State/UT'] = 'Telangana'
    df.loc[df['District'].isin(ladakh_districts), 'State/UT'] = 'Ladakh'
    return df


def process_missing_data(df):
    """
    Fills in missing data based on known relationships.
    """
    df['Population'] = df['Male'].fillna(0) + df['Female'].fillna(0)
    df['Literate'] = df['Literate_Male'].fillna(0) + df['Literate_Female'].fillna(0)
    df['Population'] = (df['Young_and_Adult'].fillna(0) + df['Middle_Aged'].fillna(0) +
                        df['Senior_Citizen'].fillna(0) + df['Age_Not_Stated'].fillna(0))
    df['Households'] = df['Households_Rural'].fillna(0) + df['Households_Urban'].fillna(0)
    return df


def load_and_clean_data(file_path, telangana_path, ladakh_districts):
    """
    Loads and cleans the census data.
    """
    df = pd.read_excel(file_path)
    df = rename_columns(df)
    df = standardize_state_names(df)

    with open(telangana_path, 'r') as file:
        telangana_districts = file.read().splitlines()

    df = handle_new_states(df, telangana_districts, ladakh_districts)
    df = process_missing_data(df)
    return df


if __name__ == "__main__":
    telangana_districts = 'data/Telangana.docx'
    ladakh_districts = ['Leh', 'Kargil']
    df = load_and_clean_data('../data/census_2011.xlsx', telangana_districts, ladakh_districts)
    df.to_csv('../data/cleaned_census_data.csv', index=False)
