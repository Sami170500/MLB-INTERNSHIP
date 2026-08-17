from collections import defaultdict, deque
import cv2

track_history = defaultdict(lambda: deque(maxlen=50))
previous_positions = {}
counted_ids = set()
class_counts = defaultdict(int)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


line_y = height // 2

output_path = "/content/tracking_counted_v2.mp4"

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
        conf=0.25,
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
        (20, line_y - 10),
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

            
            center_x = int((x1 + x2) / 2)
            center_y = int(y2)

            
            class_name = model.names[cls]

          
            previous_y = previous_positions.get(track_id)

            
            previous_positions[track_id] = center_y

            track_history[track_id].append(
                (center_x, center_y)
            )

            
            if previous_y is not None and track_id not in counted_ids:

                
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

          -
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            
            label = f"{class_name} ID:{track_id}"

            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 255, 0),
                2
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

            
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

   
    y_text = 40

    for class_name in model.names.values():

        count = class_counts[class_name]

        text = f"{class_name.capitalize()} Passed: {count}"

        cv2.putText(
            frame,
            text,
            (20, y_text),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        y_text += 30

   
    out.write(frame)

cap.release()
out.release()

print("Counting completed!")

print("\nFinal counts:")

for class_name in model.names.values():
    print(f"{class_name}: {class_counts[class_name]}")

print("\nOutput:", output_path)
