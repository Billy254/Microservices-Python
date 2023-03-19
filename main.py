from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wikilogic
from mylib.logic import search_wiki

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API: call /search or /wiki"}

@app.get("/search/{value}")
async def search(value : str):
    """Page to search in wikipedia"""
    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name : str):
    """Page to search in wikipedia"""
    result = wikilogic(name)
    return {"result": result}
    
if __name__ == "__main__":
    uvicorn.run(app, port=8082, host="0.0.0.0")
