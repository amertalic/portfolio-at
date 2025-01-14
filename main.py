import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse, name="index")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse, name="projects")
async def get_projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

if __name__ == "__main__":
    # asyncio.run(open_browser())
    uvicorn.run("main:app", port=3005, log_level="info", reload=False)