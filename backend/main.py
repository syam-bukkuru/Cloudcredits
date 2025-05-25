from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import tensorflow as tf
from PIL import Image
import numpy as np
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Cat or Dog Classification API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="cat_dog_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Image preprocessing function
def read_image(file) -> np.ndarray:
    image = Image.open(io.BytesIO(file)).convert("RGB")
    image = image.resize((160, 160))
    img_array = np.array(image) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img_batch = read_image(contents)  # Shape: (1, 160, 160, 3)

    # Run inference with TFLite
    interpreter.set_tensor(input_details[0]["index"], img_batch.astype(np.float32))
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]["index"])[0][0]

    label = "dog" if prediction > 0.5 else "cat"
    confidence = float(prediction if label == "dog" else 1 - prediction)
    return JSONResponse({"label": label, "confidence": confidence})
