# Document Text Extraction Tool

A computer vision and OCR pipeline for extracting text from document images, with preprocessing designed to handle real-world image quality issues such as tilt, blur, noise, and poor lighting.

The project combines **OpenCV** with **Tesseract OCR** to extract text while also providing the location and confidence of detected text.

## Overview

Document images captured using cameras or mobile phones may contain issues such as rotation, noise, blur, or poor lighting. These issues can affect OCR performance.

This project applies a preprocessing pipeline before OCR and also extracts text directly from the original image.

The complete pipeline is:

**Document Image → Raw OCR + Preprocessing → Preprocessed OCR → Text Detection → Bounding Boxes → Confidence Scores → TXT/JSON Results**

## Dataset

Two types of document images were used for testing:

- **Dataset images with ground-truth text** were used to demonstrate and evaluate the difference between OCR on raw and preprocessed images.
- **Three additional document images without ground truth** were used for the mandatory before/after demonstration of the preprocessing and OCR pipeline.

## Image Processing

The preprocessing stage improves the document image before text extraction.

It includes:

- Grayscale conversion
- Bilateral filtering for noise reduction
- Automatic deskewing
- CLAHE-based contrast enhancement
- Image sharpening

## OCR & Text Detection

**Tesseract OCR** is used to extract text from both the original and preprocessed images.

The preprocessed image is also used for text detection and provides:

- Extracted text
- Bounding box coordinates
- Confidence scores

Detected text regions are visualized on the processed document using bounding boxes and confidence percentages.

## Raw & Preprocessed OCR

For images with ground-truth text, OCR results from the raw and preprocessed images are compared against the correct text to demonstrate the effect of preprocessing.

For the three additional images without ground truth, numerical accuracy is not reported. Instead, the results are shown qualitatively:

**Raw Image → Preprocessed Image → OCR Output → Bounding Boxes + Confidence**

## Results

For each document, the system generates:

```text
output/
├── document_preprocessed.jpg
├── document_ocr_result.jpg
├── document_raw_extracted.txt
├── document_preprocessed_extracted.txt
└── document_ocr_data.json
