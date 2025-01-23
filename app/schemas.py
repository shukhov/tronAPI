from pydantic import BaseModel


class WalletRequest(BaseModel):
    address: str


class WalletResponse(BaseModel):
    address: str
    balance: str
    bandwidth: int
    energy: int
    created_at: str
