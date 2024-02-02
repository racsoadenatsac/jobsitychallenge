-- init_db.sql

-- Create a 'trips' table
CREATE TABLE IF NOT EXISTS trips (
    id SERIAL PRIMARY KEY,
    region VARCHAR(255) NOT NULL,
    origin_coord VARCHAR(255) NOT NULL,
    destination_coord VARCHAR(255) NOT NULL,
    datetime TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    datasource VARCHAR(255) NOT NULL
);

-- Add additional indexes if necessary for optimizing queries
-- For example, an index on the 'region' column if you'll be filtering by region often
CREATE INDEX idx_trips_region ON trips (region);

-- An index on the 'datetime' column to optimize queries filtering by time
CREATE INDEX idx_trips_datetime ON trips (datetime);
