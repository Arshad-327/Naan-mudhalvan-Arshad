import cv2

def detect_traffic_signs(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    stop_cascade = cv2.CascadeClassifier('stop_sign.xml')  # Replace with path to your classifier
    signs = stop_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in signs:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("Stop sign detected")
    return frame