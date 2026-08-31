from pathlib import Path
import cv2
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

SCALE = 4
MODEL_PATH = Path("models/RealESRGAN_x4plus.pth")

def main():
    print("=== Real-ESRGAN Image Enhancement ===")

    image_path = input("Enter image path: ").strip()
    input_path = Path(image_path)

    if not input_path.exists():
        print("Error: Image file not found.")
        return

    if not MODEL_PATH.exists():
        print(f"Error: Model not found: {MODEL_PATH}")
        return

    device = torch.device("cpu")

    print(f"Device: {device}")
    print("Loading Real-ESRGAN x4plus...")

    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=4
    )

    upsampler = RealESRGANer(
        scale=4,
        model_path=str(MODEL_PATH),
        model=model,
        tile=128,
        tile_pad=10,
        pre_pad=0,
        half=False,
        device=device
    )
  
    image = cv2.imread(str(input_path))

    if image is None:
        print("Error: Could not read image.")
        return

    print(f"Input size: {image.shape[1]} × {image.shape[0]}")
    print("Enhancing image...")

   
    output, _ = upsampler.enhance(
        image,
        outscale=SCALE
    )

    output_dir = Path("outputs/realesrgan")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{input_path.stem}_realesrgan{input_path.suffix}"

    cv2.imwrite(str(output_path), output)

    print("\nEnhancement completed!")
    print(f"Input : {input_path}")
    print(f"Output: {output_path}")
    print(f"Scale : {SCALE}x")
    print(f"Output size: {output.shape[1]} × {output.shape[0]}")
if __name__ == "__main__":
    main()
