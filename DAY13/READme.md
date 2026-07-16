
# Project Title

Object Detection using YOLOv8

---

# What is Object Detection?

Object Detection is a computer vision technique that identifies and locates multiple objects in an image. It predicts the object class and draws a bounding box around each detected object.

---

# Image Classification vs Object Detection

| Image Classification | Object Detection |
|----------------------|------------------|
| Predicts one label for the whole image. | Detects multiple objects in an image. |
| Does not locate objects. | Locates objects using bounding boxes. |
| Example: "This is a dog." | Example: Detects person, car, dog with their locations. |

---

# What is YOLO?

YOLO (You Only Look Once) is a real-time object detection algorithm. It detects multiple objects in a single pass through the image, making it fast and efficient for real-time applications.

---

# Dataset Used

Helmet Detection Dataset (Downloaded from Kaggle)

---

# Model Used

- YOLOv8 Small (yolov8s.pt)
- Pre-trained on the COCO dataset

---

# Project Steps

1. Installed the Ultralytics YOLO package.
2. Loaded the pre-trained YOLOv8s model.
3. Downloaded the Helmet Detection dataset.
4. Performed inference on the dataset images.
5. Visualized the detection results.
6. Saved the output images with bounding boxes.
7. Observed the detected objects, confidence scores, and bounding boxes.

---

# Detected Objects

The model detected several objects, including:

- Person
- Motorcycle
- Bicycle
- Car
- Truck

---

# Observations

- The model successfully detected most visible objects with bounding boxes and confidence scores.
- Output images were saved automatically in the `runs/detect/predict` folder.
- Some helmets were not detected because the pre-trained YOLOv8s model is trained on the COCO dataset, which does not include "helmet" as a detection class.
- Some small or partially hidden objects were occasionally missed or misclassified.
- Overall, the model performed fast and produced accurate detections on most images.

---

# Conclusion

This project helped me understand the fundamentals of object detection using YOLO. I learned how to perform inference with a pre-trained model, interpret bounding boxes, confidence scores, and class labels, and visualize detection results without training a custom model.



