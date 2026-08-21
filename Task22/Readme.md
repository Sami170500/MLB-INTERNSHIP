# Automatic Number Plate Recognition (ANPR)

## Overview

This project implements an Automatic Number Plate Recognition (ANPR) system that detects vehicles, detects their number plates, preprocesses the plate images, extracts plate text using OCR, overlays the recognized text on the output, and saves the results.

## Features

* Vehicle detection using a pre-trained YOLO model
* Number plate detection
* Automatic number plate cropping
* Plate image preprocessing
* Grayscale conversion
* Contrast enhancement
* OCR-based plate text extraction
* Recognized text overlay
* Plate crop saving
* OCR confidence storage
* CSV/JSON result storage
* Unreadable plate handling

## Pipeline

Input Image / Video
        ↓
Vehicle Detection
        ↓
Number Plate Detection
        ↓
Plate Cropping
        ↓
Image Preprocessing
        ↓
OCR Text Extraction
        ↓
Text Overlay
        ↓
Save Results

## Technologies Used

* Python
* OpenCV
* YOLO
* Tesseract OCR
* NumPy
* Pandas

## Preprocessing

The detected plate crops are processed before OCR to improve text recognition.

The preprocessing includes:

1. Resize
2. Grayscale conversion
3. Contrast enhancement
4. Image enhancement

## OCR

The preprocessed plate image is passed to the OCR engine to extract the number plate text and confidence score.

If the plate cannot be reliably recognized, the system marks it as:
Unreadable

## Output

The system produces:

* Detected vehicle images
* Cropped number plate images
* Recognized plate text
* OCR confidence
* Overlay results
* CSV/JSON result files

## Mandatory Challenge

The system is tested on difficult number plates, including:

* Blurry plates
* Angled plates

Difficult plates that cannot be reliably recognized are marked as `Unreadable`.

For strongly angled plates, perspective correction can be used as a future improvement to reduce perspective distortion before OCR.

## Future Improvements

* Perspective correction for angled plates
* Advanced deblurring
* Super-resolution for low-resolution plates
* Adaptive thresholding
* Multi-frame OCR for videos
* Improved OCR accuracy

## Conclusion

This project implements a complete ANPR pipeline from vehicle detection to number plate detection, preprocessing, OCR extraction, text overlay, and result storage, with handling for difficult and unreadable number plates.
