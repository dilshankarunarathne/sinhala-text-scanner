import numpy as np
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
    if image and image.content_type != "image/jpeg":
        return {300: {"description": "Only jpeg images are supported"}}
    else:
        contents = await image.read()
        nparray = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
    return {"message": "Image uploaded..."}
