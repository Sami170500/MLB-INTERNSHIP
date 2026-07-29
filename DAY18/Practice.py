import cv2
video_path = "video.mp4"  
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("fps:", fps)
print("width:", width)
print("height:", height)
print("total frames:", total_frames)
while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video.")
        break

    cv2.imshow("Original Video", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



import cv2
cap = cv2.VideoCapture("video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
format = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("processed_video.mp4", format, fps, (width, height), isColor=False)
while True:
    ret, frame = cap.read()
    if not ret:
        break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Canny Edge Detection", edges)
    out.write(edges)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()



import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
print("Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break
    cv2.imshow("Live Webcam", frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
