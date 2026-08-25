import cv2
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg"
)
folder = input("Enter image folder path: ").strip()
images = []
names = []

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    img = cv2.imread(path)

    if img is None:
        continue

    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    feature = model.predict(img, verbose=0)

    images.append(feature.flatten())
    names.append(file)

print("Images processed:", len(images))

query = input("Enter query image name: ").strip()
query = os.path.basename(query)

if query not in names:
    print("Query image not found.")
    exit()


index = names.index(query)

scores = cosine_similarity(
    [images[index]],
    images
)[0]

results = np.argsort(scores)[::-1]

top5 = []

for i in results:

    if names[i] == query:
        continue

    top5.append((names[i], scores[i]))

    if len(top5) == 5:
        break

print("\nQuery image:", query)
print("\nTop 5 similar images:")

for rank, (name, score) in enumerate(top5, 1):
    print(f"{rank}. {name} -> {score:.4f}")


results_folder = os.path.join(folder, "results")
os.makedirs(results_folder, exist_ok=True)

report = []

for rank, (name, score) in enumerate(top5, 1):

    report.append({
        "query_image": query,
        "rank": rank,
        "similar_image": name,
        "cosine_similarity": round(float(score), 4)
    })


df = pd.DataFrame(report)

df.to_csv(
    os.path.join(results_folder, "similarity_report.csv"),
    index=False
)

df.to_json(
    os.path.join(results_folder, "similarity_report.json"),
    orient="records",
    indent=4
)

plt.figure(figsize=(18, 5))

query_path = os.path.join(folder, query)

img = cv2.imread(query_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1, 6, 1)
plt.imshow(img)
plt.title("Query\n" + query)
plt.axis("off")

for i, (name, score) in enumerate(top5, 2):

    path = os.path.join(folder, name)

    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 6, i)
    plt.imshow(img)
    plt.title(f"{name}\n{score:.4f}")
    plt.axis("off")

plt.tight_layout()

output_path = os.path.join(
    results_folder,
    "top5_similarity.png"
)

plt.savefig(
    output_path,
    dpi=200,
    bbox_inches="tight"
)

plt.show()
print("\nTask A completed.")
print("Results saved in:", results_folder)
