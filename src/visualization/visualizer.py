import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine

# Database configuration - Update with your details
DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'

# Create a database engine
engine = create_engine(DATABASE_URI)

def visualize_trips_per_region():
    # Query the database for trip counts per region
    with engine.connect() as conn:
        trip_counts = pd.read_sql("""
            SELECT region, COUNT(*) as trip_count
            FROM trips
            GROUP BY region
            ORDER BY trip_count DESC
        """, conn)

    # Plot the data using seaborn
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(
        x='trip_count', 
        y='region', 
        data=trip_counts,
        palette='coolwarm'
    )

    plt.title('Number of Trips per Region')
    plt.xlabel('Number of Trips')
    plt.ylabel('Region')

    # Show the plot
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    visualize_trips_per_region()

