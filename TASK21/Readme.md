# Document Text Extraction Tool

A computer vision and OCR pipeline for extracting text from document images, with preprocessing designed to handle real-world image quality issues such as tilt, blur, noise, and poor lighting.

The project combines **OpenCV** with **Tesseract OCR** to transform a document image into searchable text while also providing the location and confidence of detected text.

## Overview

Document images captured using cameras or mobile phones are rarely perfect. A document may be slightly rotated, noisy, blurry, or affected by uneven lighting. These issues can reduce OCR performance.

This project addresses those problems by applying a preprocessing pipeline before OCR and then comparing the OCR output from the original image with the processed version.

The complete pipeline is:

**Document Image → Preprocessing → OCR → Text Detection → Bounding Boxes → Confidence Scores → TXT/JSON Results**

## Image Processing

The preprocessing stage focuses on improving the document before text extraction.

It includes:

- Grayscale conversion
- Bilateral filtering for noise reduction
- Automatic deskewing
- CLAHE-based contrast enhancement
- Image sharpening

The deskewing stage is particularly useful for documents that are photographed at an angle, while denoising and contrast enhancement help with lower-quality images.

## OCR & Text Detection

After preprocessing, **Tesseract OCR** extracts the document text.

The OCR system also provides information about individual detected text regions, including:

- Extracted text
- Bounding box coordinates
- Confidence score

These detections are visualized on the processed document using bounding boxes and confidence percentages.

## Raw vs Preprocessed OCR

One of the main parts of the project is comparing OCR performed on:

**Original Image**

versus

**Preprocessed Image**

The system records the OCR confidence for both versions and reports which version performed better.

This comparison is important because preprocessing does not automatically improve every document. A clean image may already be suitable for OCR, while preprocessing can provide a larger benefit on tilted, blurry, noisy, or poorly-lit images.

## Results

For each document, the system generates a set of files containing the processed image, OCR text, detection information, and comparison results.

```text
output/
├── document_preprocessed.jpg
├── document_raw_ocr.txt
├── document_preprocessed_ocr.txt
├── document_ocr_result.jpg
├── document_ocr_data.json
└── document_comparison.txt
