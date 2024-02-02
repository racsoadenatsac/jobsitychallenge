# Trip Data Ingestion and Visualization

This repository contains a data engineering solution for ingesting and visualizing trip data. It includes a REST API for data ingestion, a SQL database for storage, and a visualization component for generating reports.

## Project Structure

- `src/`: Source code for the project.
    - `data_ingestion/`: Data ingestion script to read CSV files and load into the database.
    - `database/`: Database models and session management.
    - `api/`: Flask REST API to trigger ingestion and serve trip data.
    - `visualization/`: Visualization scripts to generate charts from the data.
- `scripts/`: SQL scripts for initializing the database.
- `docker/`: Dockerfile and related configuration files.
- `docs/`: Documentation files.
- `tests/`: Unit tests for the application.

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker (optional for containerization)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

