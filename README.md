
# Census Data Standardization and Analysis Pipeline

This project cleans, processes, and analyzes census data from India. The goal is to ensure uniformity, accuracy, and accessibility of the census data for further analysis and visualization.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Project Structure](#project-structure)
- [Functionality](#functionality)
- [Usage](#usage)
- [Implemented Queries](#implemented-queries)
- [Additional Information](#additional-information)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- **Python:** Data processing and analysis
- **Pandas:** Data manipulation and cleaning
- **NumPy:** Numerical operations
- **MongoDB:** NoSQL database for initial data storage
- **SQLAlchemy:** ORM for database interactions
- **MySQL:** Relational database for structured query execution
- **Streamlit:** Web application framework for data visualization
- **Openpyxl:** Excel file reading

## Setup and Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/CensusDataPipeline.git
   cd CensusDataPipeline
   ```

2. **Install the required packages**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Database Connections**
   - Update the database URIs in `scripts/config.py` to match your local database configurations.

4. **Run the data cleaning script**
   ```sh
   python scripts/data_cleaning.py
   ```

5. **Save cleaned data to MongoDB**
   ```sh
   python scripts/data_storage.py
   ```

6. **Upload data to MySQL database**
   ```sh
   python scripts/data_queries.py
   ```

7. **Run the Streamlit application**
   ```sh
   streamlit run scripts/main.py
   ```

## Project Structure
```
CensusDataPipeline/
|-- data/
|   |-- census_2011.xlsx          # Raw census data file
|   |-- Telangana.txt             # Telangana districts text file
|-- scripts/
|   |-- __init__.py               # Package initializer
|   |-- config.py                 # Configuration for database connections
|   |-- data_cleaning.py          # Script for data cleaning and preprocessing
|   |-- data_storage.py           # Script for storing data in MongoDB
|   |-- data_queries.py           # Script for uploading data to MySQL
|   |-- main.py                   # Main script for running Streamlit app
|-- requirements.txt              # Python dependencies
|-- README.md                     # Project documentation
|-- .gitignore                    # Git ignore file
```

## Functionality
- **Data Cleaning:** Standardizes column names, state/UT names, handles newly formed states, and processes missing data.
- **Data Storage:** Stores cleaned data in MongoDB for initial storage and then uploads it to a MySQL database.
- **Data Analysis and Visualization:** Provides an interactive web interface using Streamlit to run queries and visualize data.

## Usage
1. **Data Cleaning and Standardization**
   - The `data_cleaning.py` script standardizes column names and state/UT names, handles the formation of new states, and processes missing data.

2. **Data Storage**
   - The `data_storage.py` script stores the cleaned data into MongoDB.

3. **Data Upload to SQL Database**
   - The `data_queries.py` script uploads the data from MongoDB to a MySQL database.

4. **Data Visualization**
   - The `main.py` script runs a Streamlit web application to visualize the data and run queries interactively.

## Implemented Queries
- **Total Population by District**
  ```sql
  SELECT District, SUM(Population) FROM census GROUP BY District;
  ```
- **Literate Population by District**
  ```sql
  SELECT District, SUM(Literate_Male), SUM(Literate_Female) FROM census GROUP BY District;
  ```
- Additional queries include:
  - Population breakdown by age group
  - Literacy rates by gender
  - Household statistics
  - Access to amenities and services

## Additional Information
- **Database Configuration:** Ensure that MongoDB and MySQL services are running locally or on accessible servers.
- **Error Handling:** Scripts include basic error handling; however, ensure database connections and file paths are correctly configured.
- **Performance Considerations:** For large datasets, optimize database queries and consider indexing frequently queried fields.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
