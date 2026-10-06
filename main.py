from fastapi import FastAPI, HTTPException
from schemas import Item
from services import id_generator
from database import get_db, urlshort
from sqlalchemy.orm import Session


app = FastAPI()


data = []

@app.get("/")
def root():
    return {"Hello":"World"}


@app.post("/urls")
def get_url(url: Item, db =  Depends(get_db)):

    short_id = id_generator()

    

    return short_id







    
