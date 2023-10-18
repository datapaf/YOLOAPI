from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import cv2
import numpy as np
import torch
# from ultralytics import YOLO

app = FastAPI()

# загрузите предварительно обученную модель YOLOv8n
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# model = YOLO("yolov8n.pt")

@app.post('/image')
def _image_upload(
        image: UploadFile = File(...),
):
    image_bytes = image.file.read()
    decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    input_image = cv2.cvtColor(decoded, cv2.COLOR_BGR2RGB)
    results = model([input_image])  # предсказать по изображению
    results.render()
    # results = model.predict(source=decoded)
    res_bytes = cv2.imencode('.jpg', results.ims[0])[1].tobytes()
    return Response(content=res_bytes, media_type="image/jpg")
