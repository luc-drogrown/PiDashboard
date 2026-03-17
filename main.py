from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from smbus2 import SMBus

app = FastAPI()
templates = Jinja2Templates(directory="templates")
bus = SMBus(1)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

