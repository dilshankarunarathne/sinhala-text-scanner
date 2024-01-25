from fastapi import APIRouter, File

router = APIRouter(
    prefix="/api/convert",
    tags=["convert"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/")
async def logout(
        image: File(...),
):
    return {"message": "Image uploaded..."}
