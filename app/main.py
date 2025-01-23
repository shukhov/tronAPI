from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import WalletRequest
from .models import get_db
from .crud import get_wallet_logs, save_wallet_log
from .tron_service import fetch_wallet_info

app = FastAPI()


@app.post("/wallet-info")
async def get_wallet_info(request: WalletRequest, db: Session = Depends(get_db)):
    try:
        wallet_info = fetch_wallet_info(request.address)
        if wallet_info:
            save_wallet_log(db, wallet_info)
            return wallet_info
        raise HTTPException(status_code=404, detail="Wallet not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/wallet-logs")
async def get_wallet_logs_api(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return get_wallet_logs(db, skip, limit)
