import cv2
from ultralytics import YOLO
from collections import defaultdict, deque

modelPath = input("Enter model path: ")
videoPath = input("Enter video path: ")
outputVideoPath = "/content/results.mp4"

LINE_Y = 400

model = YOLO(modelPath)

cap = cv2.VideoCapture(videoPath)

if not cap.isOpened():
    raise RuntimeError(f"Could not open video: {videoPath}")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

writer = cv2.VideoWriter(
    outputVideoPath,
    fourcc,
    fps,
    (width, height)
)

trackHistory = defaultdict(lambda: deque(maxlen=30))
previousPositions = {}
countedIDs = set()

classNames = model.names

classCounts = {
    classID: 0
    for classID in classNames
}

frameNumber = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frameNumber += 1

    results = model.track(
        source=frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.10,
        imgsz=640,
        device=0,
        verbose=False
    )

    result = results[0]

    cv2.line(
        frame,
        (0, LINE_Y),
        (width, LINE_Y),
        (0, 255, 255),
        3
    )

    cv2.putText(
        frame,
        "COUNTING LINE",
        (20, LINE_Y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    if result.boxes is not None and result.boxes.id is not None:

        boxes = result.boxes.xyxy.cpu().numpy()

        classes = (
            result.boxes.cls
            .cpu()
            .numpy()
            .astype(int)
        )

        trackIDs = (
            result.boxes.id
            .cpu()
            .numpy()
            .astype(int)
        )

        confidences = result.boxes.conf.cpu().numpy()

        for box, classID, trackID, confidence in zip(
            boxes,
            classes,
            trackIDs,
            confidences
        ):

            x1, y1, x2, y2 = map(int, box)

            centerX = int((x1 + x2) / 2)
            centerY = int((y1 + y2) / 2)

            className = model.names[int(classID)]

            trackHistory[trackID].append(
                (centerX, centerY)
            )

            points = list(trackHistory[trackID])

            for i in range(1, len(points)):

                cv2.line(
                    frame,
                    points[i - 1],
                    points[i],
                    (255, 0, 255),
                    2
                )

            cv2.circle(
                frame,
                (centerX, centerY),
                5,
                (255, 0, 255),
                -1
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = (
                f"{className} "
                f"ID:{trackID} "
                f"{confidence:.2f}"
            )

            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 255, 0),
                2
            )

            if trackID in previousPositions:

                previousY = previousPositions[trackID]

                crossedDown = (
                    previousY < LINE_Y
                    and centerY >= LINE_Y
                )

                crossedUp = (
                    previousY > LINE_Y
                    and centerY <= LINE_Y
                )

                crossedLine = crossedDown or crossedUp

                if (
                    crossedLine
                    and trackID not in countedIDs
                ):

                    countedIDs.add(trackID)

                    if classID in classCounts:

                        classCounts[classID] += 1

                        print(
                            f"COUNTED | "
                            f"{className} | "
                            f"ID: {trackID} | "
                            f"Total: {classCounts[classID]}"
                        )

            previousPositions[trackID] = centerY

    panelX = 20
    panelY = 30
    panelWidth = 300
    panelHeight = 70 + len(classNames) * 28

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (panelX, panelY),
        (
            panelX + panelWidth,
            panelY + panelHeight
        ),
        (0, 0, 0),
        -1
    )

    frame = cv2.addWeighted(
        overlay,
        0.55,
        frame,
        0.45,
        0
    )

    cv2.putText(
        frame,
        "TRAFFIC COUNT",
        (panelX + 15, panelY + 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    yText = panelY + 60

    for classID, className in classNames.items():

        text = f"{className}: {classCounts[classID]}"

        cv2.putText(
            frame,
            text,
            (panelX + 15, yText),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        yText += 28

    cv2.putText(
        frame,
        f"Frame: {frameNumber}/{totalFrames}",
        (width - 280, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    writer.write(frame)

    if frameNumber % 100 == 0:

        progress = (frameNumber / totalFrames) * 100

        print(
            f"Processed: "
            f"{frameNumber}/{totalFrames} "
            f"({progress:.1f}%)"
        )

cap.release()
writer.release()

print("\n======================================")
print("PROCESSING COMPLETE")
print("======================================")

print("\nFINAL COUNTS:")

for classID, className in classNames.items():
    print(
        f"{className}: "
        f"{classCounts[classID]}"
    )

print(
    "\nUnique Track IDs counted:",
    len(countedIDs)
)

print("\nOutput video:")
print(outputVideoPath)
