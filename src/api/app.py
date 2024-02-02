from flask import Flask, jsonify, request
from database import get_session
from models import Trip
from data_ingester import ingest_csv_data

app = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest_data():
    # This endpoint expects a file in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Save the file to a temporary file or process in-memory
        csv_file_path = '/tmp/tempfile.csv'
        file.save(csv_file_path)

        # Call the ingestion function from data_ingester.py
        ingest_csv_data(csv_file_path)
        return jsonify({"status": "Data ingestion completed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trips', methods=['GET'])
def get_trips():
    # This endpoint retrieves all trip records from the database
    session = get_session()
    trips = session.query(Trip).all()
    session.close()

    # Convert trip records to a list of dictionaries
    trips_data = [ 
        {
            "region": trip.region,
            "origin_coord": trip.origin_coord,
            "destination_coord": trip.destination_coord,
            "datetime": trip.datetime.isoformat(),
            "datasource": trip.datasource
        }
        for trip in trips
    ]

    return jsonify(trips_data), 200

if __name__ == '__main__':
    app.run(debug=True)

