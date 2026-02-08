import cv2
import time
import winsound

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# Start webcam (DirectShow for Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

closed_eyes_start = None
drowsy = False
last_beep_time = 0  # to avoid continuous beeping

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes_detected = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        if len(eyes) > 0:
            eyes_detected = True
            closed_eyes_start = None
            drowsy = False

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(
                    roi_color,
                    (ex, ey),
                    (ex + ew, ey + eh),
                    (0, 255, 0),
                    2
                )

    # Face detected but eyes not detected
    if len(faces) > 0 and not eyes_detected:
        if closed_eyes_start is None:
            closed_eyes_start = time.time()
        else:
            elapsed = time.time() - closed_eyes_start
            if elapsed >= 3:
                drowsy = True

    # Show alert + sound
    if drowsy:
        cv2.putText(
            frame,
            "DROWSINESS ALERT!",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        # Beep only once every 2 seconds
        current_time = time.time()
        if current_time - last_beep_time > 2:
            winsound.Beep(1000, 800)
            last_beep_time = current_time

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
