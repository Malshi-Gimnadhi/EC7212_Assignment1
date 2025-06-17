# task4.py
from PIL import Image
import numpy as np
import os

def block_average(image_path, output_path, block_size):
    """
    Replace each non-overlapping block with its average value.
    :param image_path: Path to input image
    :param output_path: Path to save output image
    :param block_size: Size of the block (e.g., 3 for 3x3)
    """
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Get image dimensions
    height, width = img_array.shape
    
    # Pad image if necessary to make dimensions divisible by block_size
    pad_height = (block_size - height % block_size) % block_size
    pad_width = (block_size - width % block_size) % block_size
    padded_array = np.pad(img_array, ((0, pad_height), (0, pad_width)), mode='edge')
    
    # Reshape to process blocks
    new_height, new_width = padded_array.shape
    blocks = padded_array.reshape(new_height // block_size, block_size,
                                 new_width // block_size, block_size)
    
    # Compute mean for each block
    block_means = blocks.mean(axis=(1, 3))
    
    # Expand means to original block size
    result = np.repeat(np.repeat(block_means, block_size, axis=0), block_size, axis=1)
    
    # Crop back to original size
    result = result[:height, :width].astype(np.uint8)
    
    # Save output image
    Image.fromarray(result).save(output_path)
    print(f"Image with {block_size}x{block_size} block averaging saved to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Test with different block sizes
    for block_size in [3, 5, 7]:
        output_path = os.path.join(output_dir, f"block_average_{block_size}x{block_size}.jpg")
        try:
            block_average(input_path, output_path, block_size)
        except Exception as e:
            print(f"Error for block_size={block_size}: {e}")

if __name__ == "__main__":
    main()