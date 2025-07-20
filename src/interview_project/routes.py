from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import PhoneSchema, OTPVerifySchema, TokenSchema
from app.services.otp import generate_otp, verify_otp
from app.crud.user import get_or_create_user
from app.core.security import create_access_token

router = APIRouter()

@router.post("/send-otp")
def send_otp(payload: PhoneSchema):
    code = generate_otp(payload.phone)
    return {"message": "OTP sent (check logs)", "otp": code}  # Normally don't return the code!

@router.post("/verify-otp", response_model=TokenSchema)
def verify(payload: OTPVerifySchema):
    if not verify_otp(payload.phone, payload.otp):
        raise HTTPException(status_code=400, detail="Invalid OTP")
    user = get_or_create_user(payload.phone)
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}