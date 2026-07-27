
# Smart Parking Lot Occupancy Analyzer

## Project Overview

The Smart Parking Lot Occupancy Analyzer is a Computer Vision project that automatically detects whether parking spaces are occupied or vacant.

The system combines traditional OpenCV image processing techniques with YOLO-based vehicle detection. Parking slot locations are obtained from COCO annotations, while YOLO detects vehicles in the parking lot. Finally, geometric analysis is used to determine whether each parking slot is occupied or empty.

---

## Features

- Load parking lot images.
- Read parking slot annotations from COCO JSON files.
- Detect vehicles using a trained YOLO model.
- Determine occupied and vacant parking spaces.
- Highlight occupied slots in **Red**.
- Highlight vacant slots in **Green**.
- Display parking occupancy statistics.
- Menu-driven and reusable application.

---

## Dataset Used

- Roboflow Parking Lot Dataset (COCO Annotation Format)

The dataset contains:

- Parking lot images
- COCO annotation file for parking slots

A custom-trained YOLO model (`best.pt`) is used for car detection.

---

## Project Workflow

1. Load Parking Lot Image
2. Read Parking Slot COCO Annotations
3. Draw Parking Slot Boundaries
4. Detect Vehicles using YOLO
5. Perform Geometric Analysis (Bounding Box Overlap)
6. Determine Occupied and Vacant Slots
7. Display Parking Statistics

---

## Image Processing Techniques Used

The project demonstrates the Computer Vision concepts learned during Days 13–17.

### OpenCV

- Image Loading
- Image Preprocessing
- Image Enhancement (CLAHE)
- Gaussian Blur
- Edge Detection (Canny)
- Morphological Operations
- Contour Detection

### YOLO

- Vehicle Detection

### Geometric Analysis

- Bounding Box Overlap
- Parking Occupancy Decision

---

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLO
- NumPy
- JSON (COCO Annotation Format)

---



---

## Menu Options


1. Load Image
2. Draw Parking Slots
3. Detect Cars
4. Check Occupancy
5. Display Statistics
6. Run Complete Pipeline
0. Exit


## Output

The application displays:

- Original Parking Image
- Parking Slot Boundaries
- YOLO Car Detection
- Occupied Parking Slots (Red)
- Vacant Parking Slots (Green)
- Parking Occupancy Statistics

---

## Results

The system successfully:

- Loaded parking lot images.
- Read parking slot annotations.
- Detected vehicles using YOLO.
- Classified parking spaces as occupied or vacant.
- Displayed overall parking occupancy statistics.

---

## Challenges Faced

- Detecting parking slots using only contour detection was not reliable because contours were detected over cars, parking lines, trees, and other objects.
- Different image conditions affected edge detection and contour extraction.
- Accurate occupancy detection required combining YOLO vehicle detection with annotated parking slot locations.
- Matching parking slot annotations with detected vehicle bounding boxes required geometric analysis.

---

## Future Improvements

- Automatic parking slot detection without annotations.
- Real-time video parking occupancy detection.
- IoU-based occupancy calculation.
- Parking availability dashboard.
- Support for multiple parking lots.
- Web or mobile application integration.





