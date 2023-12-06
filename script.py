import mysql.connector
from mysql.connector import errorcode

# MySQL connection configuration
config = {
    'user': 'root',
    'password': 'mypass',
    'host': 'localhost',
    'database': 'eco',
    'raise_on_warnings': True
}

# Function to execute queries
def execute_query(cursor, query):
    cursor.execute(query)
    cnx.commit()

# Establishing a connection to MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied. Check your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
    exit(1)

# Define table names
table_names = [
    "geolocation",
    "categories",
    "customers",
    "orderitems",
    "orderpayments",
    "orders",
    "products",
    "sellers",
    "reviews"
]

# Iterate through table names
for table_name in table_names:
    # Define CSV file path for creating tables
    csv_file_path = f'C:\ProgramData\MySQL\MySQL Server 8.0\Data\eco\{table_name}.csv'

    # SQL query to create the table
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ('

    # Open and read the first row of the CSV to get column names
    with open(csv_file_path, 'r') as file:
        header_line = file.readline().strip()
        headers = header_line.split(',')

    # Construct the CREATE TABLE query
    for header in headers:
        create_table_query += f'`{header}` VARCHAR(255), '

    create_table_query = create_table_query[:-2] + ');'

    # Execute the table creation query
    execute_query(cursor, create_table_query)

    # Define CSV file path for loading data
    csv_file_path_local = f'{table_name}.csv'
    # SQL query to load data from CSV into the table
    load_data_query = f'''
        LOAD DATA INFILE '{csv_file_path_local}'
        INTO TABLE {table_name}
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\\n'
        IGNORE 1 ROWS;
    '''

    # Execute the data loading query
    execute_query(cursor, load_data_query)

# Close the cursor and connection
cursor.close()
cnx.close()

print("Data import successful for all tables.")

