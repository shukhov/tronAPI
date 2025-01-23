from tronpy import Tron
from tronpy.exceptions import AddressNotFound


def fetch_wallet_info(address: str):
    client = Tron()
    try:
        account = client.get_account(address)
        balance = account.get("balance", 0) / 1_000_000
        bandwidth = client.get_account_bandwidth(address)
        energy = client.get_account_resource(address)["energy_used"]
        return {
            "address": address,
            "balance": str(balance),
            "bandwidth": bandwidth,
            "energy": energy,
        }
    except AddressNotFound:
        return None
