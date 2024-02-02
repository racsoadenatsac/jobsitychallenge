Install the required Python packages:


pip install -r requirements.txt
Set up the database by running the init_db.sql script on your PostgreSQL server.

Update the database connection details in src/database/database.py to match your PostgreSQL setup.

Running the Application
To start the Flask REST API, run:

python src/api/app.py
To ingest data from a CSV file, send a POST request to /ingest with the file:



curl -F 'file=@path_to_your_csv_file.csv' http://localhost:5000/ingest
To view trip data, navigate to http://localhost:5000/trips in your web browser, or use curl:



curl http://localhost:5000/trips
Visualization
Run the visualization script to generate a chart:



python src/visualization/visualizer.py
Containerization
To build a Docker image for the application, run:



docker build -t trip-data-app .
To run the application in a Docker container, use:



docker run -p 5000:5000 trip-data-app
Testing
To run tests, execute:



python -m unittest
Deployment



