import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

class palyer(BaseModel):
    number: int
    name: str
    
@app.get('/hello')
def say_hello():
    with open("hello.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

@app.get('/welcome')
def say_welcome(name: str):
    return JSONResponse(content=f"Welcome {name}!", status_code=200)

@app.post('/players')
def list_palyer(BaseModel):
      
