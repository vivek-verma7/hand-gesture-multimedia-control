# Hand Gesture Multimedia Control

A Python project that uses **MediaPipe** and **OpenCV** for real-time hand gesture recognition, allowing you to control multimedia functions such as volume, playback, and track control using gestures.

## Features

- **Fist**: Increase volume
- **Open Palm**: Decrease volume
- **Peace**: Skip to the next track
- **Point**: Go to the previous track
- **Thumbs Up**: Toggle play/pause

## Requirements

To run this project, you need to install the following Python libraries:

- **opencv-python**: For handling webcam capture and video processing.
- **mediapipe**: For hand landmark detection and gesture recognition.
- **pyautogui**: For simulating keyboard actions (controlling the multimedia).
  
You can install these libraries by running:

```bash
pip install opencv-python mediapipe pyautogui
## How to Use

1. Clone the repository or download the project files:

git clone https://github.com/vivek-verma7/hand-gesture-multimedia-control.git

markdown
Copy
Edit

2. Run the script:

python gesture_control.py

vbnet
Copy
Edit

3. The webcam window will open, and you can use the following gestures to control multimedia:

- Fist: Increase volume  
- Open Palm: Decrease volume  
- Peace: Next track  
- Point: Previous track  
- Thumbs Up: Play/Pause  

4. To exit the program, press the `q` key while the webcam window is active.

## How it Works

- The MediaPipe library is used to detect hand landmarks in real-time through the webcam feed.  
- The OpenCV library is used for image processing and displaying the webcam feed.  
- Based on detected hand gestures, PyAutoGUI simulates multimedia control actions like increasing/decreasing the volume and skipping tracks.

## Gesture Recognition Logic

- Fist: All fingers are curled towards the palm (detected by checking the relative positions of fingers and wrist).  
- Open Palm: All fingers are extended outwards.  
- Peace: The index and middle fingers are extended, while the other fingers are curled.  
- Point: The index finger is extended and others are curled.  
- Thumbs Up: The thumb is extended upwards, and the other fingers are curled.

## Cooldown Timer

To prevent continuous action from repeated gestures, a cooldown timer is set to 5 seconds. This ensures that gestures like volume control and track skipping are only triggered once every few seconds.

## Troubleshooting

- If the webcam feed is not working, make sure you have the required drivers and a functioning camera.  
- If the gestures aren’t detected accurately, ensure your hand is clearly visible and well-lit in the fra
