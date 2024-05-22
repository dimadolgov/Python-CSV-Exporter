# Flask CSV Exporter

This Flask application allows you to view CSV results from a file and export them as a separate CSV file.

## Table of Contents

- [File Structure](#file-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)

## File Structure

The project consists of the following files:

1. **app.py**: Flask application code for serving the CSV data and exporting it.
2. **index.html**: HTML template for displaying the CSV data in a table.
3. **Dockerfile**: Dockerfile for containerizing the Flask application.
4. **requirements.txt**: List of Python dependencies required by the application.

## Setup

1. Clone this repository to your local machine.

2. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have a CSV file named `results.csv` in the root directory of the project. This file will be used for displaying data.

2. Run the Flask application using the following command:

    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://localhost:5000` to view the CSV data in a table.

4. Click the "Export CSV" button to export the displayed data as a separate CSV file.

## Docker Deployment

You can also deploy this Flask application using Docker.

1. Build the Docker image using the provided Dockerfile:

    ```bash
    docker build -t flask-csv-exporter .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 5000:5000 flask-csv-exporter
    ```

3. Access the application at `http://localhost:5000` in your web browser.

