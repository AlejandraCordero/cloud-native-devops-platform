from fastapi import FastAPI

app = FastAPI(title="Mi Plataforma Cloud-Native")

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "mensaje": "Tu plataforma DevOps en la nube está funcionando perfectamente.",
        "version": "1.0.0"
    }
