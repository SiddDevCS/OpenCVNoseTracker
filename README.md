# **NoseTracker :)**

**NoseTracker :)** is a fun real-time computer vision project that uses **OpenCV** and **MediaPipe** to track your nose and create a glowing orb effect around it. The dot pulsates and changes color in response to the movement of your nose, giving it a cool interactive vibe!

## **Features**
- Tracks your **nose** in real-time using MediaPipe’s face mesh.
- Draws a **pulsing, glowing orb** that follows your nose.
- **Smooth animation** with glowing trails.
- No extra assets required, just **Python libraries** and your webcam.
- Works in real-time with live video capture.

## **Requirements**

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

### **Install Dependencies**

To install the required libraries, run:

```bash
pip install opencv-python mediapipe numpy
```

## **How to Run**

1. Clone or download this repository.
2. Open a terminal (or command prompt).
3. Navigate to the directory where your `main.py` is located.
4. Run the script using:

   ```bash
   python main.py
   ```

5. The program will open your webcam and start tracking your nose.
   - The glowing dot will follow your nose.
   - The dot will pulse and change colors dynamically as your nose moves.

6. Press **Esc** to exit the program.
