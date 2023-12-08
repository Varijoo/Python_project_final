from flask import Flask , render_template
import sqlite3
import pathlib


nnew = Flask(__name__)


base_path = pathlib.Path().cwd()
db_name = "Buisness.db"
File_path = base_path / db_name

@nnew.route("/")
def index():
    return render_template("index.html")
    
@nnew.route("/about")
def about():
    return render_template("about.html")        
    
@nnew.route("/data")
def data():
    con = sqlite3.connect(File_path)
    cursor = con.cursor()
    Celeb_Name = cursor.execute("SELECT * FROM Celeb_Name").fetchall()
    con.close()
    
    return render_template("data_table_fillin.html", Celeb_Name = Celeb_Name)    
    
    
if __name__=="__main__":
    nnew.run(debug = True)    