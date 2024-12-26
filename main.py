from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from Scripts.Twitter import get_trends 
from DB.mongodb import add_trends , get_all_trends
app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, FastAPI!"})

@app.get("/fetch_record")
async def fetch_record():
    # Fetch trends and print the result
    data = get_trends()
    saved_data = {}

    if(data != {}):
        print(data)
        saved_data =  add_trends(data)

    # return saved_data
    return saved_data
@app.get("/fetch_all_record")
async def fetch_record():
    # Fetch trends and print the result
    data = get_all_trends()

    if data is not None:
        print(data)
        return data
    else:
        return None