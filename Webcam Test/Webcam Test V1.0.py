import cv2

def capture_video(camera_index=0):
    # Open the camera
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW to avoid backend-related issues

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Display the frame
            cv2.imshow('Camera Feed', frame)

            # Break the loop when 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # By default, the code uses the first camera (index 0)
    # You can change the index if you have multiple cameras
    capture_video()
