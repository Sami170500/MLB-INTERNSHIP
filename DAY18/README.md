#  Real-Time Video Processing Tool using OpenCV

## Project Overview

This project demonstrates video processing using Python and OpenCV. The application reads a video file, processes each frame using different computer vision techniques, displays the original and processed videos, and saves the processed output as a new video.

---

## How OpenCV Reads Videos

OpenCV reads videos using the `cv2.VideoCapture()` function. A video is a collection of individual images called **frames**. The `read()` function retrieves one frame at a time, allowing image processing techniques to be applied to every frame before displaying or saving the video.

---

## What is FPS?

FPS (Frames Per Second) represents the number of frames displayed every second in a video. It determines how smooth the video appears during playback. When saving a processed video, using the same FPS as the original video helps maintain the original playback speed.

---

## Processing Techniques Applied

### Grayscale Conversion
Grayscale conversion transforms a color image into a single-channel image containing only intensity values. This simplifies image processing and reduces computational complexity.

### Gaussian Blur
Gaussian Blur smooths the image by reducing noise and small details. It is commonly applied before edge detection to improve the accuracy of the detected edges.

### Canny Edge Detection
Canny Edge Detection is an edge detection algorithm that identifies object boundaries by detecting significant intensity changes in an image. It is widely used in computer vision for feature extraction and object detection.

---

## Challenges Faced

- Understanding that a video is processed one frame at a time.
- Maintaining smooth video playback while applying multiple processing techniques.
- Preserving the original frame rate (FPS) when saving the processed video.
- Selecting suitable parameters for Gaussian Blur and Canny Edge Detection to obtain clear edge detection results.
