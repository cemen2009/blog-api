from fastapi import FastAPI

from api.v1.health.router import router as health_router


API_V1_PREFIX = "/api/v1"
API_PREFIX = API_V1_PREFIX


app = FastAPI(title="Blog API")
app.include_router(health_router, prefix=API_PREFIX, tags=["Health"])


@app.get("/")
async def root():
    return {"message": "Root endpoint is here!"}
