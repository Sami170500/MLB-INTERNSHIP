from pathlib import Path
import csv
import json
import re

import torch
import torch.nn.functional as F
from PIL import Image
import matplotlib.pyplot as plt
from transformers import CLIPProcessor, CLIPModel

IMAGE_FOLDER = Path("images")
OUTPUT_FOLDER = Path("output")
EMBEDDING_FILE = OUTPUT_FOLDER / "clip_embeddings.pt"
CAPTION_FILE = OUTPUT_FOLDER / "captions.json"

OUTPUT_FOLDER.mkdir(exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

if not EMBEDDING_FILE.exists():
    print("Error: clip_embeddings.pt not found.")
    print("Please run clip_embeddings.py first.")
    raise SystemExit

if not CAPTION_FILE.exists():
    print("Error: captions.json not found.")
    print("Please run main.py first.")
    raise SystemExit

saved_data = torch.load(
    EMBEDDING_FILE,
    map_location="cpu"
)

image_names = saved_data["image_names"]
image_embeddings = saved_data["embeddings"].to(device)

with open(CAPTION_FILE, "r", encoding="utf-8") as file:
    caption_data = json.load(file)

captions = {
    item["image"]: item["caption"]
    for item in caption_data
}

model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
).to(device)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

model.eval()


def search_images(query, top_k=5):
    inputs = processor(
        text=[query],
        return_tensors="pt",
        padding=True
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():
        text_outputs = model.text_model(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"]
        )

        text_features = model.text_projection(
            text_outputs.pooler_output
        )

    text_features = F.normalize(
        text_features,
        p=2,
        dim=-1
    )

    similarities = torch.matmul(
        text_features,
        image_embeddings.T
    )[0]

    number_of_results = min(
        top_k,
        len(image_names)
    )

    top_scores, top_indices = torch.topk(
        similarities,
        k=number_of_results
    )

    results = []

    for rank, (score, index) in enumerate(
        zip(top_scores, top_indices),
        start=1
    ):
        image_name = image_names[index.item()]

        results.append({
            "rank": rank,
            "image": image_name,
            "similarity_score": round(
                score.item(),
                4
            ),
            "caption": captions.get(
                image_name,
                "Caption not found"
            )
        })

    return results


def make_safe_filename(text):
    filename = re.sub(
        r"[^a-zA-Z0-9]+",
        "_",
        text
    ).strip("_")

    return filename[:50] or "query"


def display_results(query, results):
    fig, axes = plt.subplots(
        1,
        len(results),
        figsize=(22, 6)
    )

    if len(results) == 1:
        axes = [axes]

    for ax, result in zip(axes, results):
        image_path = IMAGE_FOLDER / result["image"]

        try:
            image = Image.open(
                image_path
            ).convert("RGB")

            ax.imshow(image)

            ax.set_title(
                f"Rank {result['rank']}\n"
                f"Score: {result['similarity_score']}\n"
                f"{result['caption']}",
                fontsize=9
            )

            ax.axis("off")

        except Exception:
            ax.set_title(
                f"Could not load\n"
                f"{result['image']}"
            )
            ax.axis("off")

    fig.suptitle(
        f'Top 5 Results for: "{query}"',
        fontsize=16
    )

    plt.tight_layout(
        rect=[0, 0, 1, 0.90]
    )

    safe_query = make_safe_filename(query)

    gallery_file = (
        OUTPUT_FOLDER /
        f"search_gallery_{safe_query}.png"
    )

    plt.savefig(
        gallery_file,
        dpi=200,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def save_results(query, results):
    csv_file = (
        OUTPUT_FOLDER /
        "search_results.csv"
    )

    csv_exists = csv_file.exists()

    with open(
        csv_file,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "query",
                "rank",
                "image",
                "similarity_score",
                "caption"
            ]
        )

        if not csv_exists:
            writer.writeheader()

        for result in results:
            writer.writerow({
                "query": query,
                "rank": result["rank"],
                "image": result["image"],
                "similarity_score":
                    result["similarity_score"],
                "caption":
                    result["caption"]
            })

    json_file = (
        OUTPUT_FOLDER /
        "search_results.json"
    )

    existing_results = []

    if json_file.exists():

        try:
            with open(
                json_file,
                "r",
                encoding="utf-8"
            ) as file:
                existing_results = json.load(file)

            if not isinstance(existing_results, list):
                existing_results = []

        except (json.JSONDecodeError, OSError):
            existing_results = []

    existing_results.append({
        "query": query,
        "results": results
    })

    with open(
        json_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            existing_results,
            file,
            indent=4,
            ensure_ascii=False
        )


while True:
    query = input(
        "Enter search query (or type 'exit' to quit): "
    ).strip()

    if query.lower() == "exit":
        break

    if not query:
        continue

    results = search_images(
        query,
        top_k=5
    )

    display_results(
        query,
        results
    )

    save_results(
        query,
        results
    )
