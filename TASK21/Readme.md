# Document Text Extraction Tool

A computer vision and OCR pipeline for extracting text from document images and evaluating the effect of image preprocessing on OCR performance.

The project combines **OpenCV** with **Tesseract OCR** to handle document images affected by tilt, blur, noise, and poor lighting. It extracts text, detects text regions, provides bounding box coordinates and confidence scores, and saves the results in TXT and JSON formats.

## Overview

Document images captured using cameras or mobile phones may contain rotation, noise, blur, and uneven lighting. These issues can affect OCR performance.

This project applies a preprocessing pipeline before OCR and also performs OCR directly on the original image.

The complete pipeline is:

**Document Image → Raw OCR + Preprocessing → Preprocessed OCR → Text Detection → Bounding Boxes + Confidence → TXT/JSON Results**

## Two Evaluation Approaches

Two approaches were used to satisfy the different requirements of the task.

### 1. Quantitative Evaluation

A document dataset containing **ground-truth text** was used to quantitatively compare OCR performance.

The same document is processed in two ways:

- OCR on the raw image
- OCR on the preprocessed image

The results are compared with the ground-truth text using:

- **WER (Word Error Rate)** – measures word-level OCR errors.
- **CER (Character Error Rate)** – measures character-level OCR errors.

This provides an objective measurement of whether the preprocessing pipeline improves OCR accuracy.

Lower WER and CER values indicate fewer OCR errors.

### 2. Qualitative Evaluation

Three separate challenging document images were selected for the mandatory before/after demonstration. These images were **not part of the ground-truth evaluation**, so numerical WER/CER accuracy was not calculated for them.

The three images were selected to represent challenging conditions such as:

- Tilted documents
- Plain text
- Poor or uneven lighting

For each image, the complete process is demonstrated:

**Raw Image → Preprocessed Image → OCR Output → Bounding Boxes + Confidence**

The results are evaluated visually by observing the improvement in document quality and OCR output.

## Image Processing

The preprocessing stage improves the document image before text extraction.

It includes:

- Grayscale conversion
- Bilateral filtering for noise reduction
- Automatic deskewing
- CLAHE-based contrast enhancement
- Image sharpening

These techniques help improve text visibility and provide a cleaner input for OCR.

## OCR & Text Detection

**Tesseract OCR** is used to extract text from both the original and preprocessed images.

Text detection provides:

- Extracted text
- Bounding box coordinates
- Confidence scores

Detected text regions are visualized on the preprocessed document using bounding boxes and confidence percentages.

## OCR Evaluation

For the ground-truth dataset, the raw and preprocessed OCR results are compared using WER and CER.

For each document, the system generates:

```text
output/
├── document_preprocessed.jpg
├── document_ocr_result.jpg
├── document_raw_extracted.txt
├── document_preprocessed_extracted.txt
└── document_ocr_data.json
