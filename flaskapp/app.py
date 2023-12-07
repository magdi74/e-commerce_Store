from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)
graphs_directory = os.path.join(app.root_path, 'static', 'images')

# function to load the graphs from images directory 
def get_graphs():
    # intialize a list to contains the images 
    graphs = []
    
    # loop in images folder and append all images files in the graphs list
    for file_name in os.listdir(graphs_directory):
        if file_name.endswith('.png'): 
            graphs.append(file_name)
    return graphs
 
# function to get a certain table information by accessing MySQL database
def get_table_data(table_name):
    # Connect to the database
    conn = mysql.connector.connect(host=os.getenv('DATABASE_HOST'), user=os.getenv('DATABASE_USERNAME'),
                                    password=os.getenv('DATABASE_PASSWORD'), database=os.getenv('DATABASE_NAME'),
                                    port=os.getenv('DATABASE_PORT'))
    cursor = conn.cursor()

    # query to select data from the table
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    conn.close()
    return data

@app.route('/')
def home():
    # render home.html "home page"
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    # get the graphs genereated by matplotlib from the notebook, then renders the dashboard.html
    graphs = get_graphs()
    return render_template('dashboard.html', graphs=graphs)

@app.route('/data')
def data():
    # render data.html
    return render_template('data.html')

@app.route('/data/<table_name>')
def tables(table_name):
    # Get the data from the table name given by the parameter then render the html page of the table name
    data = get_table_data(table_name)
    return render_template(f'{table_name}.html', data=data)
    
if __name__ == '__main__':
    app.run(debug=True)
