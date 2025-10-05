from fastapi import FastAPI, Form, Query
from jokes import jokes as jks
import sqlite3

# Connect to a persistent database file
con = sqlite3.connect('test.db', check_same_thread=False)
cur = con.cursor()

app = FastAPI(debug=False, middleware=None)

@app.get("/getAll", description= "Used to get all the Jokes from the Jokes Dictionary")
def getAllJokes():
    '''
    Method to return all the Jokes available
    '''
    result = cur.execute("SELECT * FROM jokes").fetchall()
    return {"message": "All jokes are found", "data": result}

@app.get("/getJokes/category", description= "Used to get all the Jokes under a specific category")
def getAllSinglePart(cate_name: str = Query(...)):
    '''
    Method to get all the jokes of a specific category under a specific type
    '''
    result =  cur.execute("SELECT * FROM jokes WHERE CATE_NAME=?",(cate_name,)).fetchall()
    return {"message": f"Category {cate_name} has been found", "data": result}

@app.post("/addNewJoke", description="Adds a New Joke to the DB")
def addNewJoke(cate_name: str = Form(...), type_of_joke: str = Form(...), joke: str = Form(...)):
    '''
    Method to create a new joke and add it to the DB
    '''
    # cur.execute('CREATE TABLE jokes(CATE_NAME, TYPE, JOKE)')
    cur.execute('INSERT INTO jokes VALUES(?, ?, ?)',(cate_name, type_of_joke, joke))
    # Save changes
    con.commit()
    return {"message": "New joke has been added"}
