# Python Project: Billionaire Data Website

## Group 7 - Python Group Project

### Project Description

The main goal of this project is to serve Billionaire data through a website and save it in a database. Users can access the website to view and interact with the Billionaire dataset by running the `Billionaire.py` script.

### Usage Guidelines

1. Execute `Billionaire.py` to obtain the website link.
2. Open the provided link to access the index page of the website.

### Code Samples

**Billionaire.py**

```python
from flask import Flask, render_template
import sqlite3
import pathlib

Billionaire_Html = Flask(__name__)

base_path = pathlib.Path().cwd()
db_name = "Buisness.db"
File_path = base_path / db_name

@Billionaire_Html.route("/")
def index():
    return render_template("index.html")

@Billionaire_Html.route("/about")
def about():
    return render_template("about.html")

@Billionaire_Html.route("/data")
def data():
    con = sqlite3.connect(File_path)
    cursor = con.cursor()
    Celeb_Name = cursor.execute("SELECT * FROM Celeb_Name").fetchall()
    con.close()
    return render_template("data_table_fillin.html", Celeb_Name=Celeb_Name)

if __name__ == "__main__":
    Billionaire_Html.run(debug=True)


## File Structure
- templates
  - index.html
  - about.html
  - data_table_fillin.html
- Billionaire.py
- Billionaire_Html.py
- Billionaires_Dataset.csv
- Buisness.db
- Billionair_set.ipynb



## Additional Information

- The `Health.db` file contains the SQLite database with the imported dataset. You can use a SQLite database viewer to explore the data further.

- The website is currently set to run in debug mode (`app.run(debug=True)` in `Sleep_Health_Application.py`). For production use, consider changing this configuration.

## Project Members

- **Harish Kumar Dakshinamoorthy**
- **Akash Balu**
- **Ganesh Rajendran**
