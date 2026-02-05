import cv2
import time

# Load Haar cascade classifiers
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# Start webcam (DirectShow fixes Windows MSMF issue)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

closed_eyes_start = None
drowsy = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    eyes_detected = False

    for (x, y, w, h) in faces:
        # Draw face rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

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

    # If face is detected but eyes are not detected
    if len(faces) > 0 and not eyes_detected:
        if closed_eyes_start is None:
            closed_eyes_start = time.time()
        else:
            elapsed_time = time.time() - closed_eyes_start
            if elapsed_time >= 3:
                drowsy = True

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

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
