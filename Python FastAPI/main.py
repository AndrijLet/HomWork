from fastapi import FastAPI
from api.listings import router as listings_router """підключення лістингу"""

app = FastAPI(
    title="Market API",
    version="1.0"
)

app.include_router(listings_router) """всі маршрути з listings_router додаю до мого застосунку"""


@app.get("/")
def root():
    return {"message": "API is running"}

# pip install fastapi uvicorn mysql-connector-python
# uvicorn main:app --reload