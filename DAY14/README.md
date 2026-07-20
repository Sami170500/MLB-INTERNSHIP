# Image Processing Toolkit using OpenCV

## Difference Between BGR and RGB

* **BGR (Blue, Green, Red)** is the default color format used by OpenCV.
* **RGB (Red, Green, Blue)** is the standard color format used by most image processing libraries and display systems such as Matplotlib.
* Both contain the same three color channels, but the order of the channels is different.

---

## What Are Grayscale Images and Why Are They Used?

A grayscale image contains only one channel that represents the intensity (brightness) of each pixel, ranging from **0 (black)** to **255 (white)**.

Grayscale images are used because:

* They reduce image size and memory usage.
* They simplify image processing tasks.
* They improve the speed of computer vision algorithms.
* They are commonly used in edge detection, face detection, and object detection preprocessing.

---

## OpenCV Functions Used

The following OpenCV functions were used in this project:

* `cv2.imread()` – Load an image.
* `cv2.imshow()` – Display an image.
* `cv2.waitKey()` – Wait for a key press.
* `cv2.destroyAllWindows()` – Close all image windows.
* `cv2.cvtColor()` – Convert a color image to grayscale.
* `cv2.resize()` – Resize an image.
* `cv2.rotate()` – Rotate an image.
* `cv2.flip()` – Flip an image.
* `cv2.rectangle()` – Draw a rectangle.
* `cv2.circle()` – Draw a circle.
* `cv2.line()` – Draw a line.
* `cv2.polylines()` – Draw a polygon.
* `cv2.putText()` – Add text to an image.
* `cv2.imwrite()` – Save the processed image.

---

## Challenges Faced and Solutions

### Challenge 1: Image was not loading.

**Solution:** Checked the image path and verified that the file existed before processing.

### Challenge 2: Crop operation caused errors.

**Solution:** Displayed the image width and height before asking for crop coordinates and entered valid start and end values.

### Challenge 3: Polygon drawing repeated inputs.

**Solution:** Moved the polygon drawing code outside the loop so that all points are collected first and then drawn once.

### Challenge 4: Processed images were overwritten.

**Solution:** Asked the user for a custom file name before saving each processed image.

### Challenge 5: Managing multiple images.

**Solution:** Added a **"Load New Image"** option to the menu so users can switch images without restarting the application.

