from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from enum import Enum
from .models import Task
from sqlalchemy import text
from . import crud, schemas




app = FastAPI(title = "Vrushang's FastAPI Task Management API", description = "This is a simple task management API built using FastAPI.", version = "1.0.0")

@app.get("/")
def read_root():
    return {"Welcome to the FastAPI Task Management API!"}

# @app.get("/param")
# def testing_parameter():
#     return {"message": "This is a test endpoint for parameters."}


@app.get("/param/{id}")
def testing_parameter(id : int):

    # try:
    #     id = int(id)

    # except ValueError:
    #     # return {"message": "Please provide a valid integer ID.", "status_code": 400}
    #     raise HTTPException(status_code=400, detail="Please provide a valid integer ID.")

    return {"id": id}


# @app.get("/user/{username}")
# def user_me(username : str):
#     try: 
#         number = int(username)
#         raise HTTPException(status_code=400, detail="Please provide a valid string username.")
#     except ValueError:
#         return {"user" : f"This is the {username}'s profile"}




class ModelName(str, Enum):
    Alexnet = "alexnet"
    Resnet = "resnet"
    Lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.Alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 1):
    return fake_items_db[skip : skip + limit]

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item



# @app.post("/tasks/", response_model=TaskResponse)
# def create_task(task: Task):
#     return task


@app.get("/health-db")
def health_check_db(db: Session = Depends(get_db)):

    try:
        db.execute(text("SELECT 1"))  # Simple query to check database connectivity
        return {"status": "Database connection is healthy."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")



@app.get("/product/{product_id}")
def get_product(product_id: int, q: str | None = None):
    return {"product_id": product_id, "q": q}


@app.post("/tasks/", response_model= schemas.TaskResponse, status_code= 201)

def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task_data=task)

