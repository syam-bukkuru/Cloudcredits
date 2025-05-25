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
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Cat or Dog Classification API"}

# Health check endpoint for Render
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
# Load the trained model
model = tf.keras.models.load_model("cat_dog_model.keras")

# Image preprocessing function
def read_image(file) -> np.ndarray:
    image = Image.open(io.BytesIO(file)).convert("RGB")
    image = image.resize((160, 160))
    img_array = np.array(image) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img_batch = read_image(contents)
    prediction = model.predict(img_batch)[0][0]
    label = "dog" if prediction > 0.5 else "cat"
    confidence = float(prediction if label == "dog" else 1 - prediction)
    return JSONResponse({"label": label, "confidence": confidence})

# npm run dev
# cd backend
# .\myenv\Scripts\activate
# uvicorn main:app --reload
