# Traffic Detection Project 

## Project Overview

This project is a custom traffic detection system developed using **YOLO26l**. The model detects and classifies different objects in traffic videos, including vehicles and people.

The project was developed using a custom dataset collected from different traffic video frames. The images were manually annotated in YOLO format and used to train and evaluate the model.

## Classes Detected

The model detects 6 classes:

- Bicycle
- Car
- Person
- Bike
- Truck
- Bus

## Dataset

The dataset was created from frames extracted from different traffic videos.

Initially, the dataset contained around **650 annotated images**. After evaluating the model, additional images were collected and annotated to improve performance, especially for the **Bus** class.

The final dataset contained approximately **1200 annotated images**.

The dataset was divided into:

- Training
- Validation
- Testing

Additional bus images were also added to reduce confusion between **Bus and Truck**.

## Model Training

The final model was trained using **YOLO26l** on a **Google Colab Tesla T4 GPU**.

Training configuration:

- Model: YOLO26l
- Epochs: 100
- Image size: 640 × 640
- Batch size: 8
- GPU: NVIDIA Tesla T4
- Training time: approximately 1.8 hours

The model was trained on the custom traffic dataset and then tested on unseen traffic videos.

## Results

The final model achieved the following overall validation results:

| Metric | Result |
|---|---:|
| Precision | 86.0% |
| Recall | 84.6% |
| mAP50 | 90.9% |
| mAP50-95 | 59.9% |

### Per-Class Results

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| Bicycle | 72.2% | 60.0% | 82.5% | 42.2% |
| Car | 89.8% | 89.7% | 92.0% | 66.8% |
| Person | 91.6% | 85.9% | 91.5% | 51.8% |
| Bike | 90.0% | 89.8% | 91.7% | 51.1% |
| Truck | 81.3% | 89.2% | 90.5% | 69.0% |
| Bus | 91.0% | 92.7% | 96.9% | 78.5% |

The final model performed particularly well on **Cars, Persons, Trucks, and Buses**.

## Challenges Faced

### 1. Bus and Truck Confusion

One of the main problems during testing was that some **Buses were detected as Trucks**.

This happened because the dataset had fewer examples of buses compared with some other classes.

### Solution

Additional bus images were collected and annotated. Around **75 additional images** were added to the existing dataset, and the model was retrained to improve Bus detection.

After retraining, Bus performance improved significantly:

- Precision: **91.0%**
- Recall: **92.7%**
- mAP50: **96.9%**
- mAP50-95: **78.5%**

### 2. Large Dataset Uploads

Uploading the complete dataset directly to Google Colab was time-consuming and sometimes caused the Colab session to disconnect.

Google Drive was therefore used to store and access the dataset.

### 3. Large Video Output

The prediction output videos were large because the model generated an annotated frame for every frame of the input video.

FFmpeg was used to compress the output videos and reduce their file size.

### 4. Slow Video Inference

Processing a complete traffic video can take considerable time because the model performs detection on every frame.

GPU inference was used to improve processing speed.

## Future Enhancements

The project can be further improved by:

- Adding more diverse traffic images and videos.
- Increasing the number of examples for underrepresented classes such as Bicycle.
- Collecting more difficult Bus and Truck examples.
- Improving detection in low-light and crowded traffic scenes.
- Adding vehicle tracking across video frames.
- Adding automatic vehicle counting.
- Detecting traffic density and congestion.
- Adding speed estimation.
- Deploying the model for real-time traffic monitoring.
- Optimizing the model for edge devices and real-time applications.

## Trained Model

You can download the trained model from Google Drive:

👉 **[Download YOLO26l Trained Model](https://drive.google.com/drive/folders/1DxHHoZ4YDIxaiBykDV-Ap33WALhtaHyh)**


Conclusion

The project successfully developed a custom traffic detection model using **YOLO26l**.

The final model achieved a **90.9% mAP50** and was able to detect six different traffic classes in images and videos.

The project also followed an iterative improvement process: after identifying the **Bus vs Truck** classification problem, additional bus data was collected, annotated, added to the dataset, and used for retraining.

This improved the model's ability to distinguish buses from trucks and resulted in strong final detection performance.

