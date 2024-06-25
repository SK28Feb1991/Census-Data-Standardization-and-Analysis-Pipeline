import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from config import MYSQL_DB_URI

@st.cache
def load_data():
    """
    Loads data from the SQL database.
    """
    engine = create_engine(MYSQL_DB_URI)
    query = "SELECT * FROM census"
    df = pd.read_sql(query, engine)
    return df

def total_population(df):
    """
    Calculates the total population for each district.
    """
    return df.groupby('District')['Population'].sum().reset_index()

def literate_population(df):
    """
    Calculates the literate population for each district.
    """
    return df.groupby('District')[['Literate_Male', 'Literate_Female']].sum().reset_index()

def main():
    """
    Streamlit main function to display data.
    """
    st.title("Census Data Analysis")

    df = load_data()

    st.header("Total Population by District")
    pop_data = total_population(df)
    st.write(pop_data)

    st.header("Literate Population by District")
    lit_data = literate_population(df)
    st.write(lit_data)

    # Additional queries and visualizations can be added here

if __name__ == "__main__":
    main()
