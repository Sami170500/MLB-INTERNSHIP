from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def load_image(path):
    return np.array(Image.open(path).convert("RGB"))

def calculate_metrics(original, enhanced):
    
    height = min(original.shape[0], enhanced.shape[0])
    width = min(original.shape[1], enhanced.shape[1])

    original = original[:height, :width]
    enhanced = enhanced[:height, :width]

    
    psnr = peak_signal_noise_ratio(
        original,
        enhanced,
        data_range=255
    )

    
    ssim = structural_similarity(
        original,
        enhanced,
        channel_axis=2,
        data_range=255
    )

    return psnr, ssim
print("=== Image Quality Comparison ===")


original_dir = Path(
    input("Enter original images folder: ").strip()
)

bicubic_dir = Path(
    input("Enter Bicubic results folder: ").strip()
)

realesrgan_dir = Path(
    input("Enter Real-ESRGAN results folder: ").strip()
)


results = []

for original_path in sorted(original_dir.glob("*")):

    if original_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    image_name = original_path.name
    image_stem = original_path.stem

    
    bicubic_path = bicubic_dir / f"{image_stem}_bicubic{original_path.suffix}"
    realesrgan_path = realesrgan_dir / f"{image_stem}_realesrgan{original_path.suffix}"
  
    if not bicubic_path.exists():
        print(f"Bicubic result missing: {image_name}")
        continue

    if not realesrgan_path.exists():
        print(f"Real-ESRGAN result missing: {image_name}")
        continue
  
    original = load_image(original_path)
    bicubic = load_image(bicubic_path)
    realesrgan = load_image(realesrgan_path)

   
    bicubic_psnr, bicubic_ssim = calculate_metrics(
        original,
        bicubic
    )

    realesrgan_psnr, realesrgan_ssim = calculate_metrics(
        original,
        realesrgan
    )

 
    results.append({
        "image": image_name,
        "bicubic_psnr": round(bicubic_psnr, 4),
        "realesrgan_psnr": round(realesrgan_psnr, 4),
        "bicubic_ssim": round(bicubic_ssim, 4),
        "realesrgan_ssim": round(realesrgan_ssim, 4)
    })

    print(f"Completed: {image_name}")


if len(results) == 0:
    print("No valid image pairs found.")

else:
   
    report = pd.DataFrame(results)

    
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    
    report.to_csv(
        reports_dir / "comparison_report.csv",
        index=False
    )
   
    report.to_json(
        reports_dir / "comparison_report.json",
        orient="records",
        indent=4
    )

    print("\n=== FINAL RESULTS ===")
    print(report.to_string(index=False))

    print("\nReports saved:")
    print("reports/comparison_report.csv")
    print("reports/comparison_report.json")
