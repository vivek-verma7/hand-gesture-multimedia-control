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
