from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.time_series.routes import router as time_series_router
from app.organizations.routes import router as organization_router

app = FastAPI()

origins = [
    "http://localhost:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

app.include_router(time_series_router)
app.include_router(organization_router)

@app.get("/")
def root():
    return {"": "Go to /docs to get all the api documentation"}
