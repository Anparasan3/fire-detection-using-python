import cv2
import winsound  # For Windows, you can use winsound for playing a beep sound.

from fire_detection import detect_fire

def main():
    video_capture = cv2.VideoCapture(0)  # Use 0 for default camera, adjust as needed
    alarm_active = False

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        fire_detected = detect_fire(frame)

        if fire_detected and not alarm_active:
            print("Fire detected! Activating alarm.")
            winsound.Beep(1000, 2000)  # Play a beep sound
            alarm_active = True
        elif not fire_detected and alarm_active:
            print("No fire detected. Alarm deactivated.")
            alarm_active = False

        cv2.imshow('Fire Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
