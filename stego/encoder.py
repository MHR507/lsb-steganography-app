from PIL import Image
import numpy as np

def embed_data(image_path, payload, output_path, bits=1, key=None):
    """
    Embed payload into an image using LSB steganography.
    Supports 1 or 2 bits per channel.
    """
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    # Convert payload to binary string
    data = ''.join(f'{ord(c):08b}' for c in payload)
    data_len = len(data)

    pixels = np.array(img, dtype=np.uint8).flatten()

    if data_len > len(pixels) * bits:
        raise ValueError("Payload too large for image size.")

    # Optional pixel permutation for extra security
    idx = np.random.permutation(len(pixels)) if key else np.arange(len(pixels))

    # Mask to clear last 'bits' bits
    mask = 0xFF ^ ((1 << bits) - 1)

    for i in range(data_len):
        pixels[idx[i]] &= mask              # clear LSBs
        pixels[idx[i]] |= int(data[i], 2)   # set LSB(s)

    stego_img = Image.fromarray(pixels.reshape((height, width, 3)))
    stego_img.save(output_path)
