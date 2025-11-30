import numpy as np
from PIL import Image


def embed_data(
    image_path,
    payload,
    output_path,
    bits=1,
    key=None
):
    
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    pixels = np.array(img, dtype=np.uint8).flatten()
    
    data = _convert_payload_to_binary(payload)
    data_len = len(data)
    
    _validate_payload_size(data_len, len(pixels), bits)
    
    idx = _generate_index_sequence(len(pixels), key)
    mask = _create_bit_mask(bits)
    
    _embed_bits_into_pixels(pixels, idx, data, data_len, mask)
    
    stego_img = _reconstruct_image(pixels, height, width)
    stego_img.save(output_path)


def _convert_payload_to_binary(payload):
    return ''.join(
        f'{ord(c):08b}' for c in payload
    )


def _validate_payload_size(data_len, pixel_count, bits):
    if data_len > pixel_count * bits:
        raise ValueError(
            "Payload too large for image size."
        )


def _generate_index_sequence(length, key):
    if key:
        return np.random.permutation(length)
    else:
        return np.arange(length)


def _create_bit_mask(bits):
    return 0xFF ^ ((1 << bits) - 1)


def _embed_bits_into_pixels(pixels, idx, data, data_len, mask):
    for i in range(data_len):
        pixels[idx[i]] &= mask
        pixels[idx[i]] |= int(data[i], 2)


def _reconstruct_image(pixels, height, width):
    return Image.fromarray(
        pixels.reshape((height, width, 3))
    )
