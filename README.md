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

## **How It Works**

- **MediaPipe Face Mesh**: It detects **468 landmarks** on your face, with **landmark 1** being the **tip of your nose**.
- **Glowing Dot**: The dot’s size **pulses** based on a sine wave, and its **color** changes depending on the nose position.
- The **overlay effect** uses transparency and weighted blending to create a glowing aura around the dot.

## **Customization Ideas**
Feel free to modify and add more features to this project:
- **Add more effects** like animated filters (smiles, eyebrows).
- **Change the shape** of the dot or replace it with a custom image.
- **Save screenshots** when a key is pressed, or even record a video.
- Add different tracking points for **eyes** or **mouth** to apply additional effects.

## **Credits**
- **OpenCV**: For real-time computer vision and image manipulation.
- **MediaPipe**: For the face mesh detection and tracking.
- **Python**: For building the whole system.

---

---

Let me know if you need help customizing or making the README even more awesome!
