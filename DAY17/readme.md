## What are Contours?

Contours are the boundaries or outlines of objects in an image. They are represented as a sequence of connected points that define the shape of an object. In OpenCV, contours are commonly used for object detection, shape analysis, object measurement, and image segmentation.

For example, if an image contains a rectangle, circle, and triangle, contour detection finds the outline of each shape separately.

---

## How Contour Detection Works

The contour detection process in this project follows these steps:

1. **Load the image** using `cv2.imread()`.
2. **Convert the image to grayscale** using `cv2.cvtColor()`.
3. **Apply Gaussian Blur** to reduce noise.
4. **Apply binary thresholding** to separate the objects from the background.
5. **Detect contours** using `cv2.findContours()`.
6. **Approximate the contour** using `cv2.approxPolyDP()` to reduce unnecessary points.
7. **Classify the shape** based on the number of vertices, aspect ratio, and circularity.
8. **Draw contours, bounding boxes, and labels** on the detected shapes.
9. **Calculate and display** the area and perimeter of each detected shape.
10. **Save the final output image**.

---

## Shapes Detected by the Program

The application can detect the following shapes:

- Triangle
- Square
- Rectangle
- Circle
- Pentagon
- Hexagon
- Polygon (any shape that does not match the above categories)

For each detected shape, the program:
- Draws its contour.
- Draws a bounding rectangle.
- Displays the shape name.
- Calculates and prints the area and perimeter.
- Saves the final annotated image.

---

## Challenges Faced

During the development of this project, I encountered several challenges:

- **Choosing the correct approximation value (`epsilon`)** in `cv2.approxPolyDP()`. A very small value produced too many vertices, causing rectangles and squares to be detected as polygons.
- **Distinguishing between squares and rectangles.** This was solved by calculating the aspect ratio (`width / height`) of the bounding rectangle.
- **Detecting circles accurately.** Instead of relying only on the number of vertices, circularity was used to improve circle detection.
- **Removing noise and unwanted contours.** Small contours were ignored using an area threshold to avoid detecting tiny objects.
- **Selecting suitable test images.** Images with plain backgrounds and clear geometric shapes produced the most accurate results.
