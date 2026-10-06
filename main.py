from fastapi import FastAPI, HTTPException, Depends
from schemas import Item
from services import id_generator
from database import get_db, urlshort
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi.responses import RedirectResponse


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
    

    return id

@app.get("/{id}")
def redirect(id: str, db: Session = Depends(get_db)):
    n = select(urlshort.long_url).where(urlshort.short_id == id)
    result = db.execute(n)

    a_url = result.scalar_one_or_none()

    if a_url is None:
        raise HTTPException(status_code=404, detail = "URL not found")
    
    return RedirectResponse(url=a_url)







    
