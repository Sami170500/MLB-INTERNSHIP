# Caption & Search Photo Gallery

A lightweight image captioning and semantic image search application built with pretrained **BLIP** and **CLIP** models. The project automatically generates captions for a collection of images, creates CLIP embeddings, and allows users to search the image collection using natural-language queries.

## Features

* Automatic image caption generation using **BLIP**
* CLIP-based image embeddings
* Natural-language semantic image search
* Top 5 matching image results
* Similarity score for every result
* BLIP caption displayed with each result
* Single-gallery visualization of search results
* Search results saved in CSV and JSON format
* CLIP embeddings saved for reuse
* Support for abstract and indirect search queries

## Models

| Component        | Model                                   |
| ---------------- | --------------------------------------- |
| Image Captioning | `Salesforce/blip-image-captioning-base` |
| Image Search     | `openai/clip-vit-base-patch32`          |

The base versions are used to keep the project suitable for CPU-based systems and small-scale demonstration.

## Dataset

The project uses a collection of **20 images** stored in the `images` directory.

Supported image formats:

* JPG
* JPEG
* PNG
* WEBP

## Project Structure

```text
Caption_Search_Gallery/
│
├── images/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── ...
│   └── img20.jpg
│
├── output/
│   ├── captions.csv
│   ├── captions.json
│   ├── clip_embeddings.pt
│   ├── search_results.csv
│   ├── search_results.json
│   └── search_gallery_*.png
│
├── generate_captions.py
├── clip_embeddings.py
├── search_gallery.py
└── README.md
```

## Requirements

* Python 3.10 or later
* PyTorch
* Torchvision
* Hugging Face Transformers
* Pillow
* Matplotlib

Install the dependencies:

```bash
pip install torch torchvision transformers pillow matplotlib
```

## Usage

### Generate Captions

Run:

```bash
python generate_captions.py
```

Generated captions are stored in:

```text
output/captions.csv
output/captions.json
```

### Generate CLIP Embeddings

Run:

```bash
python clip_embeddings.py
```

The generated embeddings are stored in:

```text
output/clip_embeddings.pt
```

### Search the Gallery

Run:

```bash
python search_gallery.py
```

Enter a natural-language query when prompted:

```text
Enter search query (or type 'exit' to quit):
```

Examples:

```text
a dog on the beach
a peaceful scene
something to eat
a relaxing outdoor moment
```

The application returns the five highest-ranked images and displays them together in a single gallery.

## Output Files

### `captions.csv`

Contains the image filename and automatically generated BLIP caption.

### `captions.json`

Stores image captions in structured JSON format.

### `clip_embeddings.pt`

Contains the generated CLIP image embeddings and corresponding image filenames.

### `search_results.csv`

Stores search queries, result rankings, similarity scores, image filenames, and captions.

### `search_results.json`

Stores search results in structured JSON format.

### `search_gallery_*.png`

Contains the visual Top-5 results for each search query.

## Abstract Query Evaluation

The project also evaluates CLIP using indirect queries that do not directly specify an object, such as:

```text
something to eat
a peaceful scene
a relaxing outdoor moment
```

These tests are used to assess how effectively the model handles broader semantic concepts.

## Limitations

The project is intended as a small-scale demonstration. BLIP-generated captions may not always be perfectly accurate, and abstract queries can produce weaker or less consistent similarity scores than direct object-based queries.

## Technologies

* Python
* PyTorch
* Hugging Face Transformers
* BLIP
* CLIP
* Pillow
* Matplotlib
* CSV
* JSON

## License

This project is intended for educational and demonstration purposes.

