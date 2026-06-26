from fastapi import FastAPI

from app.api.performance.performance_api import (
    router,
)

# -------------------------
# CREATE APP
# -------------------------

app = FastAPI(
    title="Performance API",
    version="1.0.0",
)

# -------------------------
# REGISTER ROUTER
# -------------------------

app.include_router(router)

# -------------------------
# ROOT
# -------------------------


@app.get("/")
async def home():

    return {
        "status": "running",
        "module": "Performance Tuning",
    }


# -------------------------
# LOCAL RUN
# -------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.api.performance.main_api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
