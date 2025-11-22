from PIL import Image
import numpy as np

def extract_data(image_path, data_length, bits=1, key=None):
    """
    Extract payload from image using manual length entry.
    Works for bits=1 or bits=2 per channel.
    :param image_path: Path to stego image
    :param data_length: Number of characters to extract (including spaces)
    :param bits: Number of LSBs used per channel
    :param key: Optional key for random pixel permutation
    :return: Extracted payload string
    """
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img, dtype=np.uint8).flatten()

    idx = np.random.permutation(len(pixels)) if key else np.arange(len(pixels))

    bits_data = ''
    total_bits = data_length * 8  # 8 bits per character

    bit_counter = 0
    pixel_index = 0

    while bit_counter < total_bits:
        # Extract 'bits' LSBs from current pixel channel
        current_bits = pixels[idx[pixel_index]] & ((1 << bits) - 1)
        # Convert to binary string, pad with zeros to ensure correct length
        bin_str = f'{current_bits:0{bits}b}'

        # Append one bit at a time
        for b in bin_str:
            if bit_counter < total_bits:
                bits_data += b
                bit_counter += 1

        pixel_index += 1

    # Convert bits back to characters
    payload = ''
    for i in range(0, len(bits_data), 8):
        byte = bits_data[i:i+8]
        payload += chr(int(byte, 2))

    return payload
