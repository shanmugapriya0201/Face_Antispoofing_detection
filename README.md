# Face_Antispoofing_detection
Facial anti-spoofing is the task of preventing false facial verification by using a photo, 
video, mask or a different substitute for an authorized person’s face. 

**Different types of attacks:** 
• Print attack: The attacker uses someone’s photo. The image is printed or 
displayed on a digital device. 
• video attack: A more sophisticated way to trick the system, which usually requires 
a looped video of a victim’s face. This approach ensures behaviour and facial 
movements to look more ‘natural’ compared to holding someone’s photo. 
• 3D mask attack: During this type of attack, a mask is used as the tool of choice for 
spoofing. It’s an even more sophisticated attack than playing a face video. In 
addition to natural facial movements, it enables ways to deceive some extra 
layers of protection such as depth sensors. 
The main objective of this project is to differentiate between the real and spoof faces. 
So how can this be done is using the Convolutional Neural Network (CNN) technique. 
Also, we use Liveness Detection algorithms to find the real and spoof faces. 

➢ Why is LIVENESS DETECTION did? 

Face Liveness Detection is a technology in face recognition which checks whether the 
image from the webcam comes from a live person or not. Face Liveness Detection is 
an essential prerequisite of Face Recognition system. In face recognition, the 
identification of an individual is done by comparing the captured images with the 
stored images of that person in real time. These recognition systems are in the rapid 
development phase and are accumulated with a new strong algorithm that improves 
the system day by day. However, these systems are facing many security issues as 
frauds are increasing on a daily basis and there is a need to upgrade these systems to 
make them more secure, reliable and automatic. 
In order to create the liveness detector, we’ll be training a deep neural network 
capable of distinguishing between real vs fake faces. 
We’ll, therefore, need to: 
• Build the image dataset. 
• Implement a CNN capable of performing liveness detector. 
• Train the liveness detector network. 
• Create a Python + OpenCV code capable of taking the trained liveness detector 
model and apply it to real-time images or videos. 
 
➢ Data Preprocessing 
Step 1: Create new directory structure for the datasets 
Step 2: Copying images into new directory structure 
Step 3: Dataset Exploration 
Step 4: Dataset Visualization 

➢ Model Preparation 
1. Choosing Framework and importing necessary libraries 
2. Load datasets and Perform image augmentations 
3. Model Selection 
4. Compiling our model 
5. Setting our model checkpoints
