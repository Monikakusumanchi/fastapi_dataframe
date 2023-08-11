from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI()

# Create a sample dataframe
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22],
    'city': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)

# FastAPI route to retrieve data
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the HTML template with the data from the dataframe
    return templates.TemplateResponse("index.html", {"request": request, "data": df.to_dict(orient='records')})

# FastAPI route to post data
@app.post("/post_data")
async def post_data(name: str = Form(...), age: int = Form(...), city: str = Form(...)):
    # Create a new row and append it to the dataframe
    new_row = {'name': name, 'age': age, 'city': city}
    global df
    df = df.append(new_row, ignore_index=True)
    return {"message": "Data posted successfully"}

# Load Jinja2 templates
templates = Jinja2Templates(directory="templates")
