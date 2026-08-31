# Image Quality Enhancement Tool

An image enhancement project that compares traditional image upscaling with AI-based super-resolution. The project uses **Bicubic Interpolation** and **Real-ESRGAN** to improve low-resolution images and evaluates their results.

## What We Did

We started with three high-quality images captured using a mobile phone. Their resolution was approximately **1280 × 853**.

To create controlled low-quality inputs, we reduced their resolution to approximately **320 × 213**. These degraded images were then enhanced back to approximately their original resolution using two different methods.

We also collected two separate real-world low-quality images for testing when the original high-quality versions were not available.

## Methods Used

### Bicubic Interpolation

Bicubic interpolation was used as the traditional baseline method. It enlarges the low-resolution image using mathematical interpolation.

### Real-ESRGAN

Real-ESRGAN x4plus was used as the AI-based super-resolution method. It uses a pre-trained deep-learning model to reconstruct and enhance details in low-resolution images.

The model was run on the CPU because CUDA was not available in the current PyTorch environment. Tiling was used to make the processing possible with available memory.

## Comparison

The enhanced images were compared with the original high-quality images using visual inspection, **PSNR**, and **SSIM**.

The visual comparison showed that Real-ESRGAN generally produced sharper and more detailed results than Bicubic.

However, the numerical evaluation gave different results. Bicubic achieved higher PSNR and SSIM scores on all three controlled images.

This demonstrates that an image can look visually sharper while still receiving a lower score from pixel-based quality metrics.

## Results

| Image | Bicubic PSNR | Real-ESRGAN PSNR | Bicubic SSIM | Real-ESRGAN SSIM |
| ----- | -----------: | ---------------: | -----------: | ---------------: |
| 1.jpg |      26.6706 |          25.0568 |       0.8671 |           0.8309 |
| 2.jpg |      19.3788 |          17.3740 |       0.4991 |           0.4557 |
| 3.jpg |      27.6241 |          26.5543 |       0.8197 |           0.7997 |

The comparison results are saved in **CSV and JSON format**, containing the results for all tested images.

## Real-World Low-Quality Images

Two additional low-quality images were used to test the enhancement methods on images where the original high-quality versions were unknown.

For these images, PSNR and SSIM cannot be calculated because there is no original reference image. Therefore, the results are evaluated visually by checking:

* Sharpness
* Visible details
* Blur
* Noise
* Artificial textures
* Enhancement artifacts

## Conclusion

The project showed that **Bicubic Interpolation** provides a strong traditional baseline and achieved better PSNR and SSIM scores on our controlled images.

**Real-ESRGAN** produced sharper and more detailed results visually, showing the advantage of AI-based super-resolution for perceptual image quality.

The project also demonstrated the importance of using both **visual evaluation and quantitative metrics** when comparing image enhancement methods.

