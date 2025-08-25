from fastapi import FastAPI, Form
from jokes import jokes as jks

app = FastAPI(debug=False, middleware=None)

@app.get("/getAll", description= "Used to get all the Jokes from the Jokes Dictionary")
def getAllJokes():
    '''
    Method to return all the Jokes available
    '''
    jokes = jks
    return {"message": "All jokes are found", "data": jokes}

@app.get("/getAll", description= "Used to get all Jokesp under category and type")
def getAllJokesOfSpecificCategory(cate_name: str = Form(...),type: str = Form(...)):
    '''
    Method to return all the jokes of a specific category
    '''
    jokes = jks[cate_name][type]
    return {"message": f"Category {cate_name} has been found", "data": jokes}

@app.get("/getAll", description= "Used to get all the Jokes under a specific category")
def getAllSinglePart(cate_name: str = Form(...)):
    '''
    Method to get all the jokes of a specific category under a specific type
    '''
    jokes = jks[cate_name]
    return {"message": f"Category {cate_name} has been found", "data": jokes}