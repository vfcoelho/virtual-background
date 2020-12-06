import cv2

def main():
    # cap = cv2.VideoCapture('/dev/video0')
    cap = cv2.VideoCapture(0)

    # configure camera for 720p @ 60 FPS
    height, width = 720, 1280
    cap.set(cv2.CAP_PROP_FRAME_WIDTH ,width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
    cap.set(cv2.CAP_PROP_FPS, 60)

    success = True

    while success:
        success, frame = cap.read()

        cv2.imwrite("test.jpg", frame)


if __name__ == "__main__":
    main()