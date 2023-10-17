from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import torch

app = FastAPI()

# загрузите предварительно обученную модель YOLOv8n
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.post('/image')
def _image_upload(
        image: UploadFile = File(...),
):
    image_bytes = image.file.read()
    decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    results = model([decoded])  # предсказать по изображению
    print(results)
    return None
