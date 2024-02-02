import pandas as pd
from sqlalchemy import create_engine

# Configuration
DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'
CSV_FILE_PATH = 'path_to_your_csv_file.csv'

# Create a database engine
engine = create_engine(DATABASE_URI)

# Define a function to ingest CSV data
def ingest_csv_data(csv_file_path, engine):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Perform any necessary transformations on the DataFrame
    # For example, you might want to convert the datetime column to a proper datetime object
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Ingest the data into the SQL database
    df.to_sql('trips', con=engine, if_exists='append', index=False)

# Run the ingestion process
if __name__ == '__main__':
    ingest_csv_data(CSV_FILE_PATH, engine)

