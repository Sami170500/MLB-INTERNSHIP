# Smart Parking Lot Occupancy Analyzer

## Project Overview

The Smart Parking Lot Occupancy Analyzer is a Computer Vision application that automatically detects parking spaces and classifies them as **Occupied** or **Vacant** using a custom-trained YOLOv8 model. The system processes parking lot images, draws colored bounding boxes around each parking space, and displays occupancy statistics.

---

## Dataset Used

- **Dataset:** PKLot Computer Vision Dataset (Roboflow)
- **Classes:**
  - space-empty
  - space-occupied
- **Total Images:** Approximately 8,280
- **Format:** YOLOv8 Object Detection

---

## Project Workflow

1. Collect and prepare the PKLot dataset.
2. Train a custom YOLOv8 model on the parking slot dataset.
3. Load the trained model (`best.pt`).
4. Allow the user to enter the image path.
5. Detect occupied and vacant parking spaces.
6. Draw:
   - **Red** bounding boxes for occupied spaces.
   - **Green** bounding boxes for vacant spaces.
7. Display parking statistics:
   - Occupied spaces
   - Vacant spaces
   - Total parking spaces

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLOv8
- Google Colab
- VS Code

---

## Results

- Successfully trained a custom YOLOv8 model on the PKLot dataset.
- Detected occupied and vacant parking spaces in parking lot images.
- Generated annotated output images with color-coded bounding boxes.
- Displayed parking occupancy statistics on the output image.

---

## Challenges Faced

- Finding a suitable parking lot dataset with correct annotations.
- Understanding the difference between YOLO Detection and YOLO Segmentation datasets.
- Resolving dataset annotation and class-label issues.
- Improving model performance by selecting the appropriate dataset and training configuration.

---

## Future Improvements

- Support real-time webcam and CCTV video analysis.
- Deploy the application using Gradio or Streamlit.
- Add parking occupancy percentage and availability indicators.
- Integrate with a smart parking management system.
- Optimize the model for faster real-time inference.

- ## Dataset Link

You can access the dataset used in this project here:

**PKLot Computer Vision Dataset (Roboflow):**  
[https://universe.roboflow.com/zoja-scekic/pklot-vsh7g](https://universe.roboflow.com/zoja-scekic/pklot-vsh7g)

---

