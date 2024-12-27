import io 
import numpy as np
from PIL import Image
import tensorflow as tf
from fastapi import FastAPI,UploadFile

# load classifier
def loading_model():
    model = tf.keras.models.load_model("image_alz_classifier.h5")
    return model 

model = loading_model()

def pred_alza(img):
  resize = tf.image.resize(img, (45,45))
  yhat= model.predict(np.expand_dims(resize/255, 0))
  id_label = []
  for i in yhat[0]:
    if i < yhat[0].max():
      id_label.append(0)
    else:
      id_label.append(1)

  id_label = id_label
  name_label = ['MildDemented','ModerateDemented','NonDemented', 'VeryMildDemented']
  temp = list(zip(id_label, name_label))
  for i in range(len(temp)):
    if temp[i][0]==1:
      label = temp[i][1]

  return(label)

app = FastAPI()

@app.post('/get_predictions')
async def get_predictions(file:UploadFile):
    image = await file.read()
    image = Image.open(io.BytesIO(image))
    response = pred_alza(image)
    return response