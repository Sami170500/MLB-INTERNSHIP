from pathlib import Path
import csv
import json

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

IMAGE_FOLDER = Path("images")
OUTPUT_FOLDER = Path("output")

OUTPUT_FOLDER.mkdir(exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")

print("\nLoading BLIP model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)

print("BLIP model loaded successfully.\n")

image_files = sorted(
    [
        file for file in IMAGE_FOLDER.iterdir()
        if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
    ]
)

print(f"Found {len(image_files)} images.\n")

results = []

for image_path in image_files:

    try:

        image = Image.open(image_path).convert("RGB")

        inputs = processor(
            images=image,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(device)
            for key, value in inputs.items()
        }

        with torch.no_grad():

            output = model.generate(
                **inputs,
                max_new_tokens=50
            )

        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )

        result = {
            "image": image_path.name,
            "caption": caption
        }

        results.append(result)

        print(f"{image_path.name}")
        print(f"Caption: {caption}")
        print("-" * 60)

    except Exception as e:

        print(f"Error processing {image_path.name}: {e}")

json_path = OUTPUT_FOLDER / "captions.json"

with open(json_path, "w", encoding="utf-8") as file:

    json.dump(
        results,
        file,
        indent=4,
        ensure_ascii=False
    )

csv_path = OUTPUT_FOLDER / "captions.csv"

with open(
    csv_path,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["image", "caption"]
    )

    writer.writeheader()
    writer.writerows(results)

print("BLIP caption generation completed.")
print(f"Captions saved to: {json_path}")
print(f"Captions saved to: {csv_path}")
