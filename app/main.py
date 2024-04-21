from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"": "Go to /docs to get all the api documentation"}
