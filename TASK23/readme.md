# Similar & Duplicate Image Finder

## Overview

This project is a **Similar & Duplicate Image Finder** built in Python. It uses two different approaches to identify images that are visually similar or nearly identical.

The project was tested on a dataset containing different images, visually similar images, and near-duplicate images.

## Task A — Similar Image Finder

For visual similarity, we used **pre-trained MobileNetV2**.

The process is:

```text
Image
↓
Resize to 224 × 224
↓
MobileNetV2
↓
Feature Embedding
↓
Cosine Similarity
↓
Top 5 Similar Images
```

MobileNetV2 was loaded with its ImageNet pretrained weights and without the final classification layer. This allows it to extract a **1280-dimensional feature embedding** for each image.

We then used **Cosine Similarity** to compare the embedding of a query image with all other images.

The system returns the **Top 5 most similar images** and their similarity scores.

It also generates a visual result showing the query image and its Top 5 matches

The results are also saved in **CSV and JSON** format.


## Task B — Duplicate & Near-Duplicate Finder

For duplicate detection, we used the **ImageHash library with Perceptual Hashing (pHash)**.

The process is:
`text
Image
↓
pHash
↓
Compare Hashes
↓
Calculate Hash Distance
↓
Find Exact / Near Duplicates


pHash represents the visual characteristics of an image as a compact hash.

The **hash distance** tells us how different two images are:

* `0` → same perceptual hash
* Small distance → visually very similar
* Large distance → more different

We used a threshold of **10** to identify near-duplicate pairs.

The system saves:

* Duplicate pairs
* Hash distances
* CSV report
* JSON report
* Visual duplicate comparison

---

## Mandatory Challenge

To test the robustness of the system, we selected one original image and created three modified versions:

1. **Resized**
2. **Cropped**
3. **Brightness changed**

The resized image was reduced to **50% of the original width and height**.

### MobileNetV2 Results

| Modification       | Cosine Similarity |
| ------------------ | ----------------: |
| Resized            |        **0.9980** |
| Brightness Changed |        **0.9908** |
| Cropped            |        **0.8591** |

These results show that MobileNetV2 successfully recognized all three modified versions as visually similar to the original.

### pHash Results

| Modification       |               pHash Distance |
| ------------------ | ---------------------------: |
| Resized            |                        **0** |
| Brightness Changed |                        **2** |
| Cropped            | Above the selected threshold |

The resized and brightness-modified images were detected as near-duplicates by pHash.

The cropped image was still recognized strongly by **MobileNetV2**, but pHash was less tolerant of the cropping operation. This demonstrates the difference between the two approaches.

## Technologies Used

* **Python**
* **OpenCV** — image processing
* **TensorFlow/Keras** — MobileNetV2
* **Scikit-learn** — Cosine Similarity
* **ImageHash** — Perceptual Hashing
* **Pandas** — CSV/JSON reports
* **Matplotlib** — visual result grids
* **Pillow** — image handling for pHash

## Final Result

The completed system can:

* Find the **Top 5 visually similar images**
* Extract **deep CNN feature embeddings**
* Calculate **Cosine Similarity**
* Detect **exact and near-duplicate images**
* Calculate **pHash distances**
* Handle modified images such as **resizing, cropping, and brightness changes**
* Generate **visual results**
* Save results in **CSV and JSON** format

