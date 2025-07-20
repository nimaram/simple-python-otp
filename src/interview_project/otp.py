import random
import logging
from datetime import datetime, timedelta

_otp_store = {}  # In-memory (use Redis in production)
logger = logging.getLogger("otp")


def generate_otp(phone: str) -> str:
    otp = str(random.randint(100000, 999999))
    _otp_store[phone] = {
        "otp": otp,
        "expires": datetime.now() + timedelta(minutes=2),
    }
    logger.info(f"OTP for {phone}: {otp}")
    return otp


def verify_otp(phone: str, otp: str) -> bool:
    record = _otp_store.get(phone)
    if record and record["otp"] == otp and datetime.now() < record["expires"]:
        del _otp_store[phone]  # one-time use
        return True
    return False
