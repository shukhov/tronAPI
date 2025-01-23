import pytest
from app.crud import save_wallet_log, get_wallet_logs
from app.models import Session, engine


@pytest.fixture
def db_session():
    session = Session(engine)
    yield session


def test_save_wallet_log(db_session):
    wallet_data = {
        "address": "test_address",
        "balance": "1000",
        "bandwidth": 500,
        "energy": 100,
    }
    log = save_wallet_log(db_session, wallet_data)
    assert log.address == "test_address"


def test_get_wallet_logs(db_session):
    logs = get_wallet_logs(db_session, 0, 10)
    assert isinstance(logs, list)
