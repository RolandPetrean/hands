from time import sleep
import cv2
import pyvirtualcam
import mp
import tensorflow as tf
import numpy as np

ifcam = input("Vrei camera (DA/NU)? ")
if ifcam == "DA":
  ifcam = True
else:
  ifcam = False

vid = cv2.VideoCapture(0)
if ifcam:
  cam = pyvirtualcam.Camera(width=640, height=480, fps=20, device="/dev/video2")

training = open('model/training.csv', 'a')
model = tf.keras.models.load_model('model/trained')
CLASSES = ["PACE", "CHILL", "PISTOL", "OK"]

def get_landmark_arrays(landmark_list):
  landmarks = [(landmark.x, landmark.y) for landmark in landmark_list.landmark]
  coordinates = [(int(x*image_width), int(y*image_height)) for (x, y) in landmarks]
  return landmarks, coordinates

while (True):
  _, frame = vid.read()
  image = frame
  image_height, image_width, _ = image.shape

  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  image, hand_landmarks = mp.process_hands(image)

  if hand_landmarks:
    for landmark_list in hand_landmarks:
      landmarks, coordinates = get_landmark_arrays(landmark_list)
      x, y, w, h = cv2.boundingRect(np.array(coordinates))
      x = max(0, x-5)
      y = max(0, y-5)
      w = min(image_width, w+5)
      h = min(image_height, h+5)
      cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
      
      probabilities = model(np.array([np.array(landmarks).flatten()]), training=False)
      prediction = np.argmax(np.squeeze(probabilities))
      class_ = CLASSES[prediction]

      if probabilities[0][prediction] < 0.5:
        continue
      cv2.putText(image, class_, (int(x+w/2-10*len(class_)), y-5), 0, 1, (0,255,0), 3)

  if ifcam:
    cam.send(image)
    cam.sleep_until_next_frame()
  else:
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('image', image)

    k = cv2.waitKey(1)
    if k == ord('q'):
      break

    for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
      if k != ord(num):
        continue
      print(num)

      training.write(num)
      for landmark in hand_landmarks:
        for landmark_list in hand_landmarks:
          landmarks, _ = get_landmark_arrays(landmark_list)
          for landmark in landmarks:
            training.write(f',{landmark[0]},{landmark[1]}')

      training.write('\n')

vid.release()
cv2.destroyAllWindows