#main entry point for the FastAPI application
from fastapi import FastAPI
from api.routes import channels
app = FastAPI()
# Include the channels router
app.include_router(channels.router, prefix="/api", tags=["channels"])
@app.get("/")
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Ethio Medical Data Warehouse API!"}
@app.get("/health")
def health_check():
    """
    Health check endpoint to verify the API is operational.
    """
    return {"status": "healthy"}
# To run the application, use the command: uvicorn api.main:app --reload
#main function to start the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, reload=True)
    