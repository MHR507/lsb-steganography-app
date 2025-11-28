import numpy as np
from PIL import Image
from scipy.stats import entropy

def extract_features(image_path):
    img = np.array(Image.open(image_path).convert("L"))  # grayscale

    total_pixels = img.size

    # 1. LSB plane
    lsb_plane = img & 1
    
    # 2. LSB histogram (normalized)
    lsb_hist = np.bincount(lsb_plane.flatten(), minlength=2).astype(float)
    lsb_hist = lsb_hist / total_pixels  # normalize

    # 3. Local binary patterns (simple LBP)
    shifted = np.roll(lsb_plane, 1, axis=1)
    lbp = (lsb_plane ^ shifted).flatten()
    lbp_hist = np.bincount(lbp, minlength=2).astype(float)
    lbp_hist = lbp_hist / total_pixels  # normalize

    # 4. Normalized run-length change ratio
    diffs = np.diff(lsb_plane.flatten())
    run_changes = np.sum(diffs != 0) / total_pixels  # normalize

    # 5. Entropy (0–1 range)
    lsb_entropy = entropy(lsb_hist + 1e-9)  # prevent log(0)

    # Final feature vector length = 2 + 2 + 1 + 1 = 6
    features = np.concatenate([
        lsb_hist,           # 2 values
        lbp_hist,           # 2 values
        np.array([run_changes, lsb_entropy], dtype=float)  # 2 values
    ])

    return features
