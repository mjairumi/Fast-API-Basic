from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Items(BaseModel):
    age: Union[int, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    sex: Union[str, None] = None
    
    
@app.get("/")
def read_root():
    data = {}
    for i in range(100):
        data[i] = i*100
    return data


@app.get("/items/{item_id}", response_model=Items)
def read_item(item_id: int, q: Union[str, None] = None):
    data =Items()
    data.age=23
    data.first_name="Mohammad"
    data.last_name="Jairumi"
    data.sex="Male"
    return data