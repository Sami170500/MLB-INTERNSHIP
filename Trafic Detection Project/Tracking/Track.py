from collections import defaultdict, deque
import cv2

CONF_THRESHOLD = 0.40
MIN_TRACK_FRAMES = 5
TAIL_LENGTH = 40

track_history = defaultdict(lambda: deque(maxlen=TAIL_LENGTH))

track_frames = defaultdict(int)

previous_positions = {}

counted_ids = set()


class_counts = defaultdict(int)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

line_y = height // 2

output_path = "/content/final_tracking_counting.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    result = model.track(
        frame,
        tracker="bytetrack.yaml",
        persist=True,
        conf=CONF_THRESHOLD,
        iou=0.50,
        verbose=False
    )[0]

    cv2.line(
        frame,
        (0, line_y),
        (width, line_y),
        (0, 0, 255),
        3
    )

    cv2.putText(
        frame,
        "COUNTING LINE",
        (20, line_y - 12),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )


    if result.boxes.id is not None:

        boxes = result.boxes.xyxy.cpu().numpy()
        track_ids = result.boxes.id.int().cpu().tolist()
        classes = result.boxes.cls.int().cpu().tolist()
        confidences = result.boxes.conf.cpu().numpy()

        for box, track_id, cls, conf in zip(
            boxes,
            track_ids,
            classes,
            confidences
        ):

            x1, y1, x2, y2 = map(int, box)

            class_name = model.names[cls]


            track_frames[track_id] += 1

           

            center_x = int((x1 + x2) / 2)
            center_y = int(y2)

            
            previous_y = previous_positions.get(track_id)

            
            previous_positions[track_id] = center_y

            
            track_history[track_id].append(
                (center_x, center_y)
            )
           
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                1
            )

                cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 0, 0),
                3
            )

            label = f"{class_name} | ID:{track_id}"

            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

        

            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

        

            points = list(track_history[track_id])

            for i in range(1, len(points)):

                cv2.line(
                    frame,
                    points[i - 1],
                    points[i],
                    (255, 0, 0),
                    3
                )

        

            if (
                previous_y is not None
                and track_frames[track_id] >= MIN_TRACK_FRAMES
                and track_id not in counted_ids
            ):

                
                crossed_down = (
                    previous_y < line_y
                    and center_y >= line_y
                )

                
                crossed_up = (
                    previous_y > line_y
                    and center_y <= line_y
                )

                if crossed_down or crossed_up:

                    counted_ids.add(track_id)

                    class_counts[class_name] += 1

    y_text = 35

    for class_name in model.names.values():

        count = class_counts[class_name]

        text = f"{class_name.capitalize()} Passed: {count}"

        cv2.putText(
            frame,
            text,
            (15, y_text),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        y_text += 28


    out.write(frame)


cap.release()
out.release()

print("Tracking + counting completed!")

print("\nFinal Counts:")

for class_name in model.names.values():

    print(
        f"{class_name.capitalize()} Passed: "
        f"{class_counts[class_name]}"
    )

print("\nOutput video:")
print(output_path)
