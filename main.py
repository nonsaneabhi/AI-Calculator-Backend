import uvicorn
from fastapi import FastAPI
from contextlib import  asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from utils.routes import router as processImage
from utils.constants import ENV, PORT, SERVER_URL

@asynccontextmanager
async def lifespan(app : FastAPI):
    yield

app = FastAPI(lifespan = lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def health():
    return {"message": "server is up and running"}

app.include_router(processImage, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))