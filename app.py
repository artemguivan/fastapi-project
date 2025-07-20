from fastapi import FastAPI, HTTPException
from db import Database
from schemas import PhraseInput, PhraseOutput

# singltone
db = Database()

app = FastAPI(title="Start app")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Start App! Go to /get to fetch a phrase."}


@app.get(
    "/get",
    response_description="Random phrase",
    description="Get random phrase from database",
    response_model=PhraseOutput,
)
async def get():
    try:
        phrase = db.get(db.get_random())
    except IndexError:
        raise HTTPException(404, "Phrase list is empty")
    return phrase

@app.post(
    "/add",
    response_description="Added phrase with *id* parameter",
    response_model=PhraseOutput,
)
async def add(phrase: PhraseInput):
    phrase_out = db.add(phrase)
    return phrase_out

@app.delete("/delete", response_description="Result of deleting")
async def delete(id: int):
    try:
        db.delete(id)
    except ValueError as e:
        raise HTTPException(404, str(e))

