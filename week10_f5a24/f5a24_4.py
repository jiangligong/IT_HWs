print("f5a24黎家暉")

import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("coffee.mp4", fourcc, 20.0, (width, height))

if not cap.isOpened():
    exit("Cannot open camera")
    
while 1:
    ret, frame = cap.read()
    if not ret:
        print("Cannot recive frame")
        break
    out.write(cv2.flip(frame, 0))
    cv2.imshow("coffee Studio", cv2.flip(frame, 0))
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()