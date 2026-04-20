# RIU4-LQP: Rotation Invariant Uniform Local Quinary Pattern

Python implementation of the RIU4-LQP algorithm for texture analysis in medical images (e.g., CT and X-ray).

---

## Research Reference

Li, H. (2025). *Enhanced Emphysema Classification in CT Images Using RIU4-LQP and Spatial Texture Features*. Proceedings of the 40th International Conference on Image and Vision Computing New Zealand (IVCNZ), Wellington, New Zealand.

---

## Overview

RIU4-LQP (Rotation Invariant Uniform Local Quinary Pattern) is a texture descriptor designed to capture local spatial patterns in images. It extends traditional local pattern methods by:

* Using quinary encoding for richer texture representation
* Incorporating rotation invariance
* Applying uniform pattern constraints to reduce dimensionality

This implementation is particularly suitable for medical image analysis tasks such as emphysema classification.

---

## Features

* Rotation-invariant texture descriptor
* Uniform pattern encoding (RIU4)
* Configurable parameters (R, P, T1, T2)
* Supports multiple LQP modes
* Batch processing support

---

## Project Structure

RIU4-LQP/
├── src/
├── examples/
├── batch/
├── data/
├── requirements.txt
└── README.md

---

## Installation

git clone https://github.com/pingpangqiu45/riu4-lqp.git
cd riu4-lqp

pip install -r requirements.txt

---

## Usage Example

```python
import numpy as np
from PIL import Image
from riu4_lqp.core import compute_RIU4_LQP

img = Image.open("data/sample_images/patch2.png").convert("L")
img_np = np.array(img)

lqp = compute_RIU4_LQP(img_np, mode='LQP1', R=1, P=8, T1=2, T2=7)

print(lqp.shape)
```

---

## Parameters

* R: Radius of circular neighborhood
* P: Number of sampling points
* mode: LQP variant (e.g., LQP1)
* T1, T2: Thresholds for quinary encoding

---

## Batch Processing

Scripts in the `batch/` folder support processing multiple images and extracting histogram-based features.

---

## Citation

@inproceedings{li2025riu4lqp,
title={Enhanced Emphysema Classification in CT Images Using RIU4-LQP and Spatial Texture Features},
author={Li, H.},
booktitle={IVCNZ},
year={2025}
}

---

## License

MIT License

