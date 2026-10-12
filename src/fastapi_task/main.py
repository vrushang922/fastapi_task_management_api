from fastapi import FastAPI



app = FastAPI(title = "Vrushang's FastAPI Task Management API", description = "This is a simple task management API built using FastAPI.", version = "1.0.0")

@app.get("/")
def read_root():
    return {"Welcome to the FastAPI Task Management API!"}


