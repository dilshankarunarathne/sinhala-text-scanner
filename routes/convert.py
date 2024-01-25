from datetime import timedelta

from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends, File
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    prefix="/api/convert",
    tags=["convert"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/")
async def logout(
        image: File(...),
):
    return {"message": "Successfully logged out"}
