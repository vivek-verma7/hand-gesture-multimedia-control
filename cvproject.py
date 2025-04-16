import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Gesture mapping to actions
gesture_actions = {
    "fist": lambda: pyautogui.press("volumeup"),
    "open_palm": lambda: pyautogui.press("volumedown"),
    "peace": lambda: pyautogui.press("nexttrack"),
    "point": lambda: pyautogui.press("prevtrack"),
    "thumbs_up": lambda: pyautogui.press("playpause")
}

last_gesture = None
last_gesture_time = 0
cooldown_time = 5
volume_gestures = {"fist", "open_palm"}

def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]
    
    if all(finger.y > wrist.y for finger in [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip]):
        return "fist"
    elif all(finger.y < wrist.y for finger in [index_tip, middle_tip, ring_tip, pinky_tip]):
        return "open_palm"
    elif index_tip.y < wrist.y and middle_tip.y < wrist.y and ring_tip.y > wrist.y and pinky_tip.y > wrist.y and thumb_tip.y > wrist.y:
        return "peace"
    elif index_tip.y < wrist.y and all(finger.y > wrist.y for finger in [middle_tip, ring_tip, pinky_tip]):
        return "point"
    elif thumb_tip.y < wrist.y and index_tip.y > thumb_tip.y:
        return "thumbs_up"
    else:
        return "unknown"

# Start webcam capture
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            gesture = recognize_gesture(landmarks)
            
            current_time = time.time()
            if gesture in volume_gestures:
                action = gesture_actions.get(gesture, lambda: print("Unknown gesture"))
                action()
            elif gesture != "unknown" and (gesture != last_gesture or last_gesture == "thumbs_up") and (current_time - last_gesture_time > cooldown_time):
                action = gesture_actions.get(gesture, lambda: print("Unknown gesture"))
                action()
                last_gesture = gesture
                last_gesture_time = current_time
            
            cv2.putText(frame, f"Gesture: {gesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(f"Detected Gesture: {gesture}")
    
    cv2.imshow("Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()