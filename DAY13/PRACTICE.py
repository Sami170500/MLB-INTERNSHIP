from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.info()
results = model.predict(
    source="pics",
    conf=0.7,
    save=True,
    show=True
)
for result in results:
    for box in result.boxes:

        class_id = int(box.cls)

        print("Object :", result.names[class_id])
        print("Confidence :", float(box.conf))
        print("Bounding Box :", box.xyxy.tolist())
        print("-" * 30)
