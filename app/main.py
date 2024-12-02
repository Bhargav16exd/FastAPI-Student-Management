from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .routers.students import router as students

from .db import initiate_database

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students, tags=["students"])


