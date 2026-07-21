# Document Image Enhancement Tool

## Transformations Implemented

### 1. Image Loading
- Implemented image loading using OpenCV (`cv2.imread()`).
- The user can provide an image path, and the program reads the document image for further processing.

### 2. Image Rotation / Tilt Correction
- Implemented rotation correction to fix tilted or scanned document images.
- This transformation helps align the document properly and improves readability.

### 3. Grayscale Conversion
- Converted colored document images into grayscale using `cv2.cvtColor()`.
- Grayscale removes unnecessary color information and focuses on intensity values, making further processing easier.

### 4. Image Thresholding / Binarization
- Applied thresholding techniques to separate text from the background.
- This improves text visibility by making the document background cleaner.

### 5. Noise Reduction
- Applied noise removal techniques to reduce unwanted spots and small distortions.
- This helps create a cleaner document image.

### 6. Image Sharpening
- Used sharpening techniques to enhance edges and make text clearer.
- This improves the quality of scanned documents, especially blurry text.

### 7. Output Saving
- Implemented automatic saving of processed images.
- Each enhanced image is stored separately instead of replacing previous outputs.

---

## Purpose of Enhancement Techniques

| Technique | Purpose |
|-----------|---------|
| Rotation Correction | Fixes tilted documents and improves alignment |
| Grayscale Conversion | Removes color information and simplifies processing |
| Thresholding | Improves contrast between text and background |
| Noise Reduction | Removes unwanted marks and improves clarity |
| Sharpening | Enhances text edges and makes characters clearer |
| Saving Output | Keeps processed images for future use |

---

## Transformation With Biggest Impact

The transformation that had the biggest impact on document quality was **thresholding combined with grayscale conversion**.

Grayscale conversion removed unnecessary color information, while thresholding increased the difference between text and background. This made the document easier to read and improved the overall appearance.

---

## Challenges Faced During Implementation

### 1. Managing Multiple Images
- Initially, new processed images replaced previous outputs.
- Solved this by creating unique filenames and saving every output separately.

### 2. Handling Different Image Qualities
- Some images had different lighting conditions, noise, and blur.
- Adjusted enhancement techniques to improve readability.

### 3. Understanding OpenCV Functions
- Learning different OpenCV functions and their parameters was challenging.
- Solved this by testing each transformation individually and observing the results.

### 4. Image Path and File Handling
- Incorrect paths caused image loading failures.
- Added checks to verify whether the image was loaded successfully before processing.

---

## Conclusion

This project helped understand how computer vision techniques can improve document images. Using OpenCV transformations such as grayscale conversion, thresholding, noise removal, and sharpening, the quality and readability of scanned documents were improved.
