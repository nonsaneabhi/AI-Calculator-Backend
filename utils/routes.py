import base64
from PIL import Image
from io import BytesIO
from fastapi import APIRouter
from pydantic import BaseModel
from .utils import analyze_image

class ImageData(BaseModel):
    image: str
    variables: dict

router = APIRouter()

@router.post('')
async def initiate(data: ImageData):
    imageData = base64.b64decode(data.image.split(',')[1])
    imageBytes = BytesIO(imageData)
    image = Image.open(imageBytes)
    responses = analyze_image(image, data.variables)
    data = []
    for response in responses:
        data.append(response)
        print(response)
    return {
        "message": "Canvas has been processed",
        "type": "success",
        "data": data
    }