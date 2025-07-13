import cv2
import numpy as np
import os
import serial
import time
import pyttsx3

# === TTS Setup ===
engine = pyttsx3.init()
engine.setProperty("rate", 140)
def speak(text): engine.say(text); engine.runAndWait()

# === Face Recognition Training ===
data_path = r"C:\Users\vanas\OneDrive\Desktop\3rdyear\images"
files = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]
training_data, labels = [], []

for i, file in enumerate(files):
    img = cv2.imread(os.path.join(data_path, file), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        resized_img = cv2.resize(img, (200, 200))  # Resize for consistency
        training_data.append(resized_img)
        labels.append(i)

# Convert labels to int32 as required by OpenCV
labels = np.array(labels, dtype=np.int32)

# Create and train recognizer
model = cv2.face.LBPHFaceRecognizer_create()
model.train(training_data, labels)
print("Training complete.")

# === Haar Cascade Classifier ===
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    print("Faces detected:", len(faces))  # Debugging line

    if len(faces) == 0:
        return img, None

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Optional: draw box
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
        return img, roi

    return img, None

# === Webcam Recognition ===
cap = cv2.VideoCapture(0)
unlocked, not_match, not_found = 0, 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from camera")
        break

    img, face = detect_face(frame)

    if face is not None:
        try:
            face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            label, confidence = model.predict(face_gray)
            conf = int((1 - confidence / 300) * 100)
            cv2.putText(img, f"{conf}%", (100, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if conf > 50:
                cv2.putText(img, "Unlocked", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                unlocked += 1
            else:
                cv2.putText(img, "Locked", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                not_match += 1
        except Exception as e:
            print("Prediction error:", str(e))
            cv2.putText(img, "Prediction Error", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            not_found += 1
    else:
        cv2.putText(img, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        not_found += 1

    cv2.imshow('Face Recognition', img)

    if cv2.waitKey(1) == 13 or unlocked >= 5 or not_match >= 30 or not_found >= 20:
        break

cap.release()
cv2.destroyAllWindows()

# === Arduino + Audio Feedback ===
if unlocked >= 5:
    speak("Face matched. Unlocking door.")
    try:
        ard = serial.Serial('COM9', 9600)
        time.sleep(2)
        ard.write(b'a')  # Send unlock signal
        time.sleep(5)
        speak("Door is closing.")
    except:
        speak("Arduino not connected.")
elif not_match >= 30:
    speak("Face is not matching. Please try again.")
elif not_found >= 20:
    speak("Face not found. Please try again.")

