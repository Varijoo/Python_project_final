## Python_project_final

# Group 7 - Python Group Project

# Project Description: 
The main goal of this project is to serve Billionaire data through a website and save it in a database. Users can access the website to view and interact with the Billionaire dataset by running the Billionaire.py script.

## Usage Guidelines:
Execute Billionaire.py to obtain the website link.
Open the provided link to access the index page of the website.

## Code Samples:
Billionaire.py

from flask import Flask , render_template
import sqlite3
import pathlib


Billionair_Html = Flask(__name__)


base_path = pathlib.Path().cwd()
db_name = "Buisness.db"
File_path = base_path / db_name

@Billionair_Html.route("/")
def index():
    return render_template("index.html")
    
@Billionair_Html.route("/about")
def about():
    return render_template("about.html")        
    
@Billionair_Html.route("/data")
def data():
    con = sqlite3.connect(File_path)
    cursor = con.cursor()
    Celeb_Name = cursor.execute("SELECT * FROM Celeb_Name").fetchall()
    con.close()
    return render_template("data_table_fillin.html", Celeb_Name = Celeb_Name)

    
    
if __name__=="__main__":
    Billionair_Html.run(debug = True)    


  ##  File Structure:
templates

Billionair_set.ipynb

Billionaire.py

Billionaire_Html.py

Billionaires_Dataset.csv

Buisness.db
