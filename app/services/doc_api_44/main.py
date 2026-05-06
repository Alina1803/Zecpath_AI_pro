from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import interview44, report44

# Initialize FastAPI app
app = FastAPI(
    title="HR Interview AI API",
    description="API for AI-powered HR interview system",
    version="1.0.0"
)

# Enable CORS (important for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(interview44.router, prefix="/api/v1", tags=["Interview"])
app.include_router(report44.router, prefix="/api/v1", tags=["Report"])


# Health Check
@app.get("/")
def root():
    return {"message": "HR Interview AI Running"}


# Optional: Health endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}