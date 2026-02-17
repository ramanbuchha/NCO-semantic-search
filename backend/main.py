from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .search import semantic_search, exact_search, metadata
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="NCO Semantic Search API")

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later we can restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "NCO Semantic Search Backend Running"}

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/data")
def get_data():
    return metadata[:200]   # sending limited for safety


@app.get("/exact_search")
def exact_search_api(query: str):
    return exact_search(query)


@app.get("/semantic_search")
def semantic_search_api(query: str, k: int = 10):
    return semantic_search(query, k)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=9000, reload=False)
