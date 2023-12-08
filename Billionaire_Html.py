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