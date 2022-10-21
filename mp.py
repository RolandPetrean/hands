import mediapipe as mp
import cv2

drawing = mp.solutions.drawing_utils
drawing_styles = mp.solutions.drawing_styles

hands = mp.solutions.hands.Hands()
def process_hands(image):
  results = hands.process(image)

  hand_landmarks = results.multi_hand_landmarks
  if hand_landmarks:
    for i, landmark_list in enumerate(hand_landmarks):
      drawing.draw_landmarks(image, landmark_list, mp.solutions.hands.HAND_CONNECTIONS, drawing_styles.get_default_hand_landmarks_style(), drawing_styles.get_default_hand_connections_style())
  
  return image, hand_landmarks