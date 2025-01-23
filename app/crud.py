from sqlalchemy.orm import Session
from .models import WalletLog


def save_wallet_log(db: Session, wallet_data: dict):
    log = WalletLog(**wallet_data)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_wallet_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(WalletLog).offset(skip).limit(limit).all()
