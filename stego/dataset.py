import os
import random
import string
from stego.encoder import embed_data
from stego.features import extract_features
import numpy as np

def random_payload(length=50):
    """Generate a random payload string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

def generate_dataset(cover_folder="images/cover", stego_folder="images/stego", bits=1, num_stego_per_cover=5, payload_length=50):
    """
    Generate dataset of features for cover and stego images.
    
    :param cover_folder: folder containing cover images
    :param stego_folder: folder to save stego images
    :param bits: LSB bits to use for embedding
    :param num_stego_per_cover: number of stego variants per cover image
    :param payload_length: length of random payload for embedding
    :return: X (features), y (labels)
    """
    os.makedirs(stego_folder, exist_ok=True)
    cover_images = [f for f in os.listdir(cover_folder) if f.endswith(".png")]
    X, y = [], []

    for img_name in cover_images:
        cover_path = os.path.join(cover_folder, img_name)
        
        # Extract cover features once
        cover_features = extract_features(cover_path)
        X.append(cover_features)
        y.append(0)

        # Generate multiple stego images per cover
        for i in range(num_stego_per_cover):
            payload = random_payload(payload_length)
            stego_path = os.path.join(stego_folder, f"{i}_{img_name}")
            embed_data(cover_path, payload, stego_path, bits=bits)

            stego_features = extract_features(stego_path)
            X.append(stego_features)
            y.append(1)

    return np.array(X), np.array(y)
