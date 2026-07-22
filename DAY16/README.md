# Day 16 – Edge Detection & Morphological Operations

## Difference Between Sobel, Laplacian, and Canny

### Sobel Operator

* Detects edges in the horizontal (X) and vertical (Y) directions.
* Provides information about the direction of edges.
* Best for detecting edges in a specific direction.

### Laplacian Operator

* Detects edges in all directions using the second derivative.
* Produces thin edges but is more sensitive to noise.
* Does not provide edge direction.

### Canny Edge Detection

* Multi-stage edge detection algorithm.
* Applies Gaussian Blur, gradient calculation, non-maximum suppression, and double thresholding.
* Produces clean, accurate, and continuous edges.
* Best choice for document boundary detection.

---

# Purpose of Each Morphological Operation

### Erosion

* Shrinks white objects.
* Removes small white noise.
* Separates touching objects.

### Dilation

* Expands white objects.
* Fills small gaps.
* Connects broken objects.

### Opening (Erosion → Dilation)

* Removes small white noise while preserving the main object.
* Used for image cleaning.

### Closing (Dilation → Erosion)

* Fills small holes and gaps.
* Connects broken edges.
* Makes document boundaries continuous.

### Morphological Gradient

* Extracts the boundary of objects.
* Useful for contour and shape detection.

### Top Hat

* Highlights small bright objects.
* Used for enhancing bright details.

### Black Hat

* Highlights small dark objects.
* Used for detecting dark details and defects.

---

# Best Combination of Techniques

The best results for document boundary detection were achieved using:

1. Convert image to Grayscale.
2. Apply Gaussian Blur to remove noise.
3. Detect edges using Canny Edge Detection.
4. Apply Morphological Closing to connect broken edges.
5. Detect the largest contour.
6. Draw the detected boundary on the original image.

This combination produced the most accurate and continuous document boundaries.

---

# Challenges Faced During Document Boundary Detection

* Some document images had shadows and uneven lighting.
* Thin text and document edges were difficult to detect.
* Choosing the correct Canny threshold values required experimentation.
* Kernel size affected the quality of morphological operations.
* Some images contained multiple contours, making it difficult to identify the document boundary.
* High-quality, high-contrast images produced the best results.

