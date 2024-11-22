from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# 將 "static" 資料夾掛載為靜態檔案伺服目錄
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def read_root():
    return {
        "message": "Welcome! Access static files at /static/<filename>",
        "example": "http://127.0.0.1:8000/static/README.md"
    }

if __name__ == "__main__":
    print("Server is running at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
