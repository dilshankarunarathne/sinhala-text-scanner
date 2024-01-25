from datetime import timedelta

from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    prefix="/api/convert",
    tags=["convert"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    """
    The endpoint for logging out a user

    Args:
        token (oauth2 bearer token): the token for the user

    Returns:
        (dict) The message for logging out
    """
    blacklist_token(token)
    return {"message": "Successfully logged out"}
