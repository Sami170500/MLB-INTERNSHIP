# YOLOv8 Instance Segmentation: Scratch vs Pretrained
We created a small custom **instance segmentation dataset** for detecting **bottles**.

- Images were manually annotated using **MakeSense.ai**
- Polygon masks were created for each bottle
- Annotations were exported in **YOLO segmentation format**
- Dataset was divided into training and validation sets
- 44 images were used for training
- 12 images were used for validation
- 11 additional unseen images were used for final testing

## Models

We trained two YOLOv8n-seg models using the same dataset and the same training settings.

### Model 1 — From Scratch

The first model was trained with **random weights**.

### Model 2 — COCO Pretrained

The second model started from **YOLOv8n-seg COCO pretrained weights** and was fine-tuned on our bottle dataset.

## Training Settings

Both models used:

- YOLOv8n-seg
- 50 epochs
- Image size: 416
- Batch size: 8
- Tesla T4 GPU
- Same training dataset
- Same validation dataset
- Same settings for a fair comparison

## Results

| Metric | From Scratch | COCO Pretrained |
|---|---:|---:|
| Mask mAP50 | 0.0479 | **0.7900** |
| Mask mAP50-95 | 0.0275 | **0.6040** |
| Training Time | 4.85 min | **4.52 min** |
| Average Inference Time | 0.2280 sec/image | **0.1738 sec/image** |

## Unseen Image Testing

Both models were tested on the same **11 unseen images**.

### From Scratch

- Total inference time: **2.5083 seconds**
- Average inference time: **0.2280 seconds/image**

### COCO Pretrained

- Total inference time: **1.9115 seconds**
- Average inference time: **0.1738 seconds/image**

## What We Found

The **COCO pretrained model performed much better** than the model trained from scratch.

The biggest difference was in segmentation accuracy:

- Scratch Mask mAP50-95: **0.0275**
- Pretrained Mask mAP50-95: **0.6040**

The pretrained model also had better Mask mAP50 and was faster during our unseen-image inference test.

## Conclusion

Training from scratch on a very small dataset was not effective because the model had to learn visual features from random weights using only a small number of images.

The COCO pretrained model already had useful learned visual features, so it adapted much better to our bottle segmentation task.

**Final conclusion: YOLOv8n-seg with COCO pretrained weights performed significantly better than training YOLOv8n-seg from scratch on our small custom dataset.**

## Tools Used

- Python
- Ultralytics YOLOv8
- YOLOv8n-seg
- MakeSense.ai
- Google Colab
- NVIDIA Tesla T4
- YOLO Segmentation Format
```

