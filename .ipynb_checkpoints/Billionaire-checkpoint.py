from flask import Flask , render_template
import pandas as pd
import sqlite3
import pathlib

path = pathlib.Path().cwd()

def create_db(db_name , filename , table_name):
    
    file_path = path/ filename
    
    con = sqlite3.connect('Buisness.db')
    cursor = con.cursor()
    
    Celeb_Name = pd.read_csv('Billionaires_Dataset.csv') 
    Celeb_Name.to_sql(table_name , con , index = False, if_exists="replace")
    
    result = cursor.execute("SELECT * FROM Celeb_Name").fetchall()
    print(result)

    con.commit()
    con.close()
    

if __name__=="__main__":
    db_name = "Buisness.db"
    filename = "Billionaires_Dataset.csv"
    table_name = "Celeb_Name"
    create_db(db_name, filename, table_name)