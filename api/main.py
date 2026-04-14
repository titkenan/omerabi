# api/main.py  ← dosyanın en başında, en üstte olsun
# @vercel/python
from fastapi import FastAPI
# geri kalan kodların...
from fastapi import FastAPI
# geri kalan kodların...
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Ömer Abi API",
    description="Vercel'de şahane çalışıyor",
    version="1.0.0"
)

# CORS (gerekirse)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Ömer Abi Vercel'de şahane çalışıyor amk"}

# Mevcut endpoint'larını buraya taşıyabilirsin ya da
# from omerabi.main import app as app2  şeklinde merge yaparsın ama şimdilik bu yeter
