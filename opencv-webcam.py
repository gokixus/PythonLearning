import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("videos/self_video.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width,height))

while True:
    ret,frame = cap.read()

    cv2.imshow("Video",frame)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()