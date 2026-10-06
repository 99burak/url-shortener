from fastapi import FastAPI, HTTPException, Depends
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
def get_url(url: Item, db: Session = Depends(get_db)):
    
    id = id_generator()
    new_url = urlshort(
        long_url = url.url,
        short_id = id
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    

    return new_url







    
