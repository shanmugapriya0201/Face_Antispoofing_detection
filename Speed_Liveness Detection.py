import cv2 
from tensorflow.keras.preprocessing.image import img_to_array 
import os 
import numpy as np 
from tensorflow.keras.models import model_from_json 
from tqdm import tqdm 
import time 
 
root_dir = os.getcwd() 
 
face_cascade = 
cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml") 
 
json_file = open('antispoofing_models/intern
project_antispoofing_model_mobilenet.json','r') 
loaded_model_json = json_file.read() 
json_file.close() 
model = model_from_json(loaded_model_json) 
# antispoofing model weights  
model.load_weights('antispoofing_models/intern-project_antispoofing_model_95
0.820000.h5') 
print("Model loaded ") 
 
for img in tqdm(os.listdir(os.path.join(root_dir,'test'))): 
    t1 = time.time() 
    img_arr = cv2.imread(os.path.join(root_dir,'test',img)) 
    resized_face = cv2.resize(img_arr,(160,160)) 
    resized_face = resized_face.astype("float") / 255.0 
     
    resized_face = np.expand_dims(resized_face, axis=0) 
    
    preds = model.predict(resized_face)[0] 
    if preds > 0.68: 
        label = 'spoof' 
        t2 = time.time() 
        print( 'Time taken was {} seconds'.format( t2 - t1)) 
    else: 
        label = 'real' 
        t2 = time.time() 
        print( 'Time taken was {} seconds'.format( t2 - t1)) 
