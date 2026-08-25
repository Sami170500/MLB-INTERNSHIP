import cv2
import os
import imagehash
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

folder = input("Enter image folder path: ")

files = os.listdir(folder)
hashes = {}

for file in files:
    path = os.path.join(folder, file)
    img = cv2.imread(path)

    if img is None:
        continue

    hashes[file] = imagehash.phash(Image.open(path))

duplicates = []

names = list(hashes.keys())

for i in range(len(names)):
    for j in range(i + 1, len(names)):

        distance = hashes[names[i]] - hashes[names[j]]

        if distance <= 10:
            duplicates.append([
                names[i],
                names[j],
                distance
            ])

print("\nNear-duplicate pairs:", len(duplicates))

for item in duplicates:
    print(f"{item[0]} <-> {item[1]} | distance = {item[2]}")

results_folder = os.path.join(folder, "results")
os.makedirs(results_folder, exist_ok=True)

df = pd.DataFrame(
    duplicates,
    columns=["image1", "image2", "hash_distance"]
)

df.to_csv(
    os.path.join(results_folder, "duplicate_report.csv"),
    index=False
)

df.to_json(
    os.path.join(results_folder, "duplicate_report.json"),
    orient="records",
    indent=4
)

if duplicates:

    count = min(len(duplicates), 5)

    plt.figure(figsize=(12, 5 * count))

    for i in range(count):

        name1, name2, distance = duplicates[i]

        img1 = cv2.imread(os.path.join(folder, name1))
        img2 = cv2.imread(os.path.join(folder, name2))

        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        plt.subplot(count, 2, i * 2 + 1)
        plt.imshow(img1)
        plt.text(
            10, 30,
            name1,
            color="white",
            fontsize=12,
            backgroundcolor="black"
        )
        plt.axis("off")

        plt.subplot(count, 2, i * 2 + 2)
        plt.imshow(img2)
        plt.text(
            10, 30,
            f"{name2} | Distance: {distance}",
            color="white",
            fontsize=12,
            backgroundcolor="black"
        )
        plt.axis("off")

    plt.subplots_adjust(
        left=0.02,
        right=0.98,
        top=0.98,
        bottom=0.02,
        hspace=0.15,
        wspace=0.05
    )

    plt.savefig(
        os.path.join(results_folder, "duplicate_results.png"),
        dpi=200,
        bbox_inches="tight"
  )

    plt.show()
print("\nResults saved in:")
print(results_folder)
