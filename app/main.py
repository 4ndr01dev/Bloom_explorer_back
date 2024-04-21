from fastapi import FastAPI
from app.time_series.routes import router as time_series_router

app = FastAPI()

app.include_router(time_series_router)


@app.get("/")
def root():
    return {"": "Go to /docs to get all the api documentation"}
