from pathlib import Path
from PIL import Image
SCALE = 4
def main():
    print("=== Bicubic Image Enhancement ===")

    image_path = input("Enter image path: ").strip()

    input_path = Path(image_path)

   
    if not input_path.exists():
        print("Error: Image file not found.")
        return
   
    try:
        image = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
  
    new_width = image.width * SCALE
    new_height = image.height * SCALE
    
    enhanced = image.resize(
        (new_width, new_height),
        Image.Resampling.BICUBIC
    )
   
    output_dir = Path("outputs/bicubic")
    output_dir.mkdir(parents=True, exist_ok=True)
  
    output_path = output_dir / f"{input_path.stem}_bicubic{input_path.suffix}"

    enhanced.save(output_path)

    print("\nEnhancement completed!")
    print(f"Input : {input_path}")
    print(f"Output: {output_path}")
    print(f"Scale : {SCALE}x")
    print(f"Original size : {image.size}")
    print(f"Enhanced size : {enhanced.size}")

if __name__ == "__main__":
    main()
