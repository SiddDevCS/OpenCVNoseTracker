import cv2
import mediapipe as mp
import numpy as np

import math
import time

# mediapipe setup
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False,
                                  max_num_faces=1,
                                  refine_landmarks=True,
                                  min_detection_confidence=0.5,
                                  min_tracking_confidence=0.5)

# webcam setup and all

cap = cv2.VideoCapture(0)

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks: # check if faces are detected

        for face_landmarks in results.multi_face_landmarks: # for each detected face
            h, w, _ = frame.shape # get frame width/ height
            nose = face_landmarks.landmark[1] # nose
            cx, cy = int(nose.x * w), int(nose.y * h)

            # draw glowing orb effect (pulsing circle)
            pulse = int(10 + 5 * math.sin(time.time() * 4))
            for i in range(5, 0, -1):
                radius = pulse + i * 4
                alpha = int(255 / (i + 1))
                color = (255 - i * 30, 100 + i * 15, 255)
                overlay = frame.copy()
                cv2.circle(overlay, (cx, cy), radius, color, -1)
                cv2.addWeighted(overlay, 0.05, frame, 0.95, 0, frame)

            cv2.circle(frame, (cx, cy), 6, (255, 255, 255), -1)

    # title
    cv2.putText(frame, 'NoseTracker :)', (20, 40),
         cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 255, 200), 2)

    cv2.imshow("NoseTracker :)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # esc to exit
        break

cap.release()
cv2.destroyAllWindows()
