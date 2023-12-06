from flask import Flask, render_template
import os

app = Flask(__name__)
graphs_directory = os.path.join(app.root_path, 'static', 'images')

def get_graphs():
    graphs = []
    for file_name in os.listdir(graphs_directory):
        if file_name.endswith('.png'): 
            graphs.append(file_name)
    return graphs
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    graphs = get_graphs()
    return render_template('dashboard.html', graphs=graphs)

@app.route('/data')
def data():
    return render_template('data.html')
    
if __name__ == '__main__':
    app.run(debug=True)
