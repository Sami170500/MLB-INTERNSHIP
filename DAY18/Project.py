import cv2
print("1. Process Video File")
print("2. Process Webcam")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    video_path = input("Enter the video file path: ")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(" Wrong Path")
        exit()

elif choice == "2":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(" Unable to access the webcam.")
        exit()

else:
    print("Invalid choice.")
    exit()

Output_path = input("Enter the output video path: ")
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    Output_path,
    fourcc,
    fps,
    (width, height),
    isColor=False
)
if not out.isOpened():
    print("Error: VideoWriter could not open.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Processing completed.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)

    cv2.imshow("Original", frame)
    cv2.imshow("Processed", edges)

    out.write(edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
