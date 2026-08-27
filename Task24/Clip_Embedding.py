from pathlib import Path
import torch
import torch.nn.functional as F
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

IMAGE_FOLDER = Path("images")
OUTPUT_FOLDER = Path("output")

OUTPUT_FOLDER.mkdir(exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")

print("\nLoading CLIP model...")

model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
).to(device)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

model.eval()

print("CLIP model loaded successfully.\n")

image_files = sorted(
    [
        file
        for file in IMAGE_FOLDER.iterdir()
        if file.suffix.lower() in [
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
        ]
    ]
)

print(f"Found {len(image_files)} images.\n")

embeddings = []
image_names = []
for image_path in image_files:

    try:

        image = Image.open(image_path).convert("RGB")
