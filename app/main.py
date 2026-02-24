from fastapi import FastAPI

app = FastAPI(title="Fraud Investigation API")

@app.get("/")
def root():
    return {"message": "Fraud Investigation API", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}
