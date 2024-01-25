from datetime import timedelta

from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

"""
    API router for auth endpoint
    
    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        [POST] /api/auth/register
        register_user: the endpoint for registering a new user

        [POST] /api/auth/login
        login_for_access_token: the endpoint for logging in a user

        [POST] /api/auth/logout
        logout: the endpoint for logging out a user
"""

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
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
