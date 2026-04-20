
import numpy as np
import pandas as pd
import os
from PIL import Image
from tqdm import tqdm



# === Reuse LQP code blocks (assume already defined) ===
# - threshold_func()
# - circular_1_segments()
# - compute_index()
# - compute_RIU4_LQP()


# === Parameters ===
P = 8

max_code = P * P + 11  # Total histogram bins per channel: 75



# image_dir = = "C:\\Users\\haipeng\\Downloads\\00_IVCNZ2025\\00_CTED_database\\patches_png\\patch2.png"

image_dir = "C:\\Users\\patches_png\\"


# image_dir = './patches/'  # Directory where patch1.png ... patch168.png are stored


output_csv = 'C:\\Users\\patches_png\\riu4_lqp_histograms.csv'




# === Column Names for Output CSV ===
columns = []
for c in range(1, 5):  # Channels: c1 to c4
    for f in range(max_code):  # Code bins: f0 to f74
        columns.append(f'c{c}_f{f}')




# === Collect Histograms from All Images ===
histogram_rows = []

for i in tqdm(range(1, 169), desc="Processing images"):
    filename = f'patch{i}.png'
    image_path = os.path.join(image_dir, filename)

    
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img_np = np.array(img)

    row = []
    for mode in ['LQP1', 'LQP2', 'LQP3', 'LQP4']:
        desc = compute_RIU4_LQP(img_np, mode=mode, R=1, P=8, T1=2, T2=7)
        hist, _ = np.histogram(desc, bins=np.arange(max_code + 1))  # bins from 0 to 75
        row.extend(hist.tolist())  # Add 75 values for this channel

    histogram_rows.append(row)



# === Write to CSV ===
df = pd.DataFrame(histogram_rows, columns=columns)

df.to_csv(output_csv, index=False)

print(f"Histogram CSV saved to: {output_csv}")


