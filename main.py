from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

class ImageUpload(BaseModel):
    images: List[UploadFile]
    chat_id: int  

def extract_truck_details(local_file_path):
    #we need to code for processing the image
    return "nothing as of now"

@app.get("/")
async def welcome():
    return {"message":"Welcome to OCR project"}

@app.post("/logTruck")
async def ocr_bilti_image(images: List[UploadFile] = File(...)):
    try:
        for image in images:
            # Save the image locally
            local_file_path = f"uploads/{image.filename}"
            with open(local_file_path, "wb") as f:
                f.write(image.file.read())

            # Access the chat ID using images.chat_id
            chat_id = images.chat_id

            # Process the image to extract required data
            if extract_truck_details(local_file_path):
                print(f"Data from the image {image.filename} has been extracted successfully!")

            # Clean up: Delete the local file
            os.remove(local_file_path)

        return JSONResponse(content={"message": "Data from the image has been extracted successfully!"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

