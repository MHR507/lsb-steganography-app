import numpy as np
from PIL import Image
from scipy.stats import skew, kurtosis

def extract_features(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img).reshape(-1,3)
    
    mean = np.mean(pixels, axis=0)
    var = np.var(pixels, axis=0)
    skewness = skew(pixels, axis=0)
    kurt = kurtosis(pixels, axis=0)

    # LSB plane analysis
    lsb_plane = np.unpackbits(pixels, axis=1)[:,-1]
    ones_ratio = np.sum(lsb_plane) / lsb_plane.size

    return np.concatenate([mean, var, skewness, kurt, [ones_ratio]])
