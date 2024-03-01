import cv2 
from tensorflow.keras.preprocessing.image import img_to_array 
import os 
import numpy as np 
from tensorflow.keras.models import model_from_json 
 
root_dir = os.getcwd() 
 
face_cascade = 
cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml") 
#  Anti-Spoofing Model graph 
json_file = open('antispoofing_models/intern
project_antispoofing_model_mobilenet.json','r') 
loaded_model_json = json_file.read() 
json_file.close() 
model = model_from_json(loaded_model_json) 
 
#  antispoofing model weights  
model.load_weights('antispoofing_models/intern-project_antispoofing_model_95
0.820000.h5') 
print("Model loaded") 
 
#lst=[] 
video = cv2.VideoCapture(0) 
while True: 
    try: 
        ret,frame = video.read() 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray,1.3,5) 
        for (x,y,w,h) in faces:   
            face = frame[y-6:y+h+6,x-6:x+w+6] 
            #resized_face = cv2.resize(faces,(0,0), None,0.30,0.30) 
            resized_face = cv2.resize(face,(160,160)) 
 
            resized_face = resized_face.astype("float") / 255.0 
             
            resized_face = np.expand_dims(resized_face, axis=0) 
             
            preds = model.predict(resized_face)[0] 
            print(preds) 
            #lst.append(preds) 
            if preds > 0.68: 
                label = 'spoof[FAKE]' 
                cv2.putText(frame, label, (x,y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2) 
                cv2.rectangle(frame, (x, y), (x+w,y+h), 
                    (0, 0, 255), 2) 
            else: 
                label ='real[ORIGINAL]' 
                cv2.putText(frame, label, (x,y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2) 
                cv2.rectangle(frame, (x, y), (x+w,y+h), 
                (0, 255, 0), 2) 
        cv2.imshow('frame', frame) 
        key = cv2.waitKey(1) 
        if key == ord('d'): 
            break 
    except Exception as e: 
        pass 
#print(lst) 
video.release()         
cv2.destroyAllWindows()
