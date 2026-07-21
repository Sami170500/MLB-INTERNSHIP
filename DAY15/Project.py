import cv2
import numpy as np
img = None
while True:
    print("\n===== Document Image Enhancement Tool =====")
    print("1. Load Image")
    print("2. Convert the tilted image")
    print("3. Convert to Grayscale")
    print("4. Reduce Noise")
    print("5. Enhance Brightness & Contrast")
    print("6. Sharpen Image")
    print("7. Save Image")
    print("8. Show Image")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        path = input("Enter image path: ")
        img = cv2.imread(path)

        if img is None:
            print("Image not found")
        else:
            print("Image Loaded Successfully.")
    elif choice == "2":

     if img is None:
        print("Load an image first.")

     else:
        print("Enter the four corner coordinates of the document")
        x1 = int(input("Top Left x: "))
        y1 = int(input("Top Left y: "))
        x2 = int(input("Top Right x: "))
        y2 = int(input("Top Right y: "))
        x3 = int(input("Bottom Left x: "))
        y3 = int(input("Bottom Left y: "))
        x4 = int(input("Bottom Right x: "))
        y4 = int(input("Bottom Right y: "))
        pts1 = np.float32([
            [x1, y1],
            [x2, y2],
            [x3, y3],
            [x4, y4]
        ])

        pts2 = np.float32([
            [0, 0],
            [400, 0],
            [0, 600],
            [400, 600]
        ])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)

        img = cv2.warpPerspective(img, matrix, (400, 600))
        print("Perspective Corrected Successfully.")


    elif choice == "3":

        if img is None:
            print("Load an image first.")
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print("Converted to Grayscale.")

    elif choice == "4":

        if img is None:
            print("Load an image first.")
        else:
            img = cv2.medianBlur(img,3)
            print("Noise Reduced.")

    elif choice == "5":

        if img is None:
            print("Load an image first.")
        else:
            img = cv2.convertScaleAbs(img, alpha=1.2, beta=10)
            print("Brightness & Contrast Enhanced.")

    elif choice == "6":

        if img is None:
            print("Load an image first.")
        else:

            kernel = np.array([
                [0,-1,0],
                [-1,5,-1],
                [0,-1,0]
            ])

            img = cv2.filter2D(img,-1,kernel)
            print("Image Sharpened.")

    elif choice == "7":

     if img is None:
        print("No image to save.")

     else:
        filename = input("Enter output file name: ")

        cv2.imwrite(f"outputs/{filename}.jpg", img)

        print("Image Saved Successfully.")

    elif choice == "8":

        if img is None:
            print("Load an image first.")
        else:
            cv2.imshow("Image",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    elif choice == "9":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
