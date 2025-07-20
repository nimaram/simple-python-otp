from pydantic import BaseModel
from datetime import datetime

class PhoneSchema(BaseModel):
    phone: str

class OTPVerifySchema(PhoneSchema):
    otp: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str