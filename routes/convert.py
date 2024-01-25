import cv2
import numpy as np

from fastapi import APIRouter, File, UploadFile

from ocr.scan_image import scan_image
from singlish.converter import singlish_to_english
from translate.translator import translate_text

router = APIRouter(
    prefix="/api/convert",
    tags=["convert"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("")
async def logout(
        image: UploadFile = File(...)
):
    if image and image.content_type != "image/jpeg":
        return {300: {"description": "Only jpeg images are supported"}}
    else:
        contents = await image.read()
        nparray = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    singlish_text = scan_image(img)

    english_text = singlish_to_english(singlish_text)

    final_text = translate_text(english_text)

    return {"text": final_text}
