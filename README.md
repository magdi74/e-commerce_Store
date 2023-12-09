# Ecommerce Store

## Flask App

This is a simple web blog application built with Flask and mysql-connector-python in Python 3. Users can view all the tables in the database and click on the title of a table to view its contents. Users can view some insights created with matplotlib in the dashboard.

### Installation

To run this app, you will need:

- Python 3 and pip installed on your system

To set up the app, follow these steps:

1. Clone this repository to your local machine: `https://github.com/magdi74/e-commerce_Store.git`
2. open .env file and change this variables 
3. Set the environment variables for the database connection: `DATABASE_HOST=your_host DATABASE_USERNAME=your_username DATABASE_PASSWORD=your_password DATABASE_NAME=your_name DATABASE_PORT=your_port`
4. Navigate to the project directory: `cd flaskapp`
5. Install the required packages: `pip install -r requirements.txt`
6. Run the app: `python app.py`

### Usage

Once the app is running, you can access it from your browser at `http://localhost:5000`.

- To view the home page, go to `/`
- To view the dashboard page, go to `/dashboard`
- To view the data page, go to `/data`
- To view a specific table page, go to `/data/<table_name>`


## Flask App with Docker
This repository contains a Flask web application that has been containerized using Docker for easy deployment and scalability. The Flask app serves on port 5000, and the Docker image can be pulled and run effortlessly. Follow the steps in the README to set up and access the application locally.


### Installation

1. Pull the Docker Image `docker pull magdy74/flaskapp`
2. Run the Docker Container `docker run -p 5000:5000 magdy74/flaskapp`
3. Open your web browser and go to http://localhost:5000

## Script File
A Python script that imports data from CSV files into a MySQL database. The data is related to an e-commerce platform and contains information about geolocation, categories, customers, order items, order payments, orders, products, sellers, and reviews.
Prerequisites


### Installation


To run this project, you need to have the following installed on your system:
-	Python 3
-	MySQL Server 8.0
-	mysql-connector-python


You also need to have a database named eco and a use your user name and password.


### Usage


To run the script, follow these steps:
1. Navigate to the project directory: `cd python_script_for_data`
2. Copy the CSV files from the data folder to the `.\ProgramData\MySQL\MySQL Server 8.0\Data\eco` folder
3.	Run the script with the command python `script.py`
4.	Wait for the script to finish and check the output message
The script will create tables for each CSV file and load the data into them. You can verify the results by connecting to the eco database and querying the tables.


## Ecommerce Project Notebook


This notebook is part of the Ecommerce Project, a Python script that imports data from CSV files into a MySQL database. The data is related to an e-commerce platform and contains information about geolocation, categories, customers, order items, order payments, orders, products, sellers, and reviews.


The notebook performs the following tasks:
1.	Connects to the MySQL database and queries the data tables
2.	Reads the data into pandas dataframes and performs some data preparation steps
3.	Conducts some exploratory data analysis and generates plots using matplotlib


### Prerequisites


To run this notebook, you need to have the following installed on your system:
-	Python 3
-	Jupyter Notebook
-	MySQL Server 8.0
-	mysql-connector-python
-	pandas
-	matplotlib

   
### Usage


To run the notebook, follow these steps:
1.	Navigate to the project directory `cd jupyter_notebook`
2.	Launch Jupyter Notebook with the command `jupyter notebook`
3.	Open the notebook file `Ecommerce Dataset.ipynb`
4.	Run the cells in order or use the Run All option from the Cell menu
5.	View the results and plots in the notebook


## Contributing

If you want to contribute to this project, you can:

- Fork this repository and create a new branch
- Make your changes and commit them
- Push your branch and create a pull request
- Wait for feedback and approval


