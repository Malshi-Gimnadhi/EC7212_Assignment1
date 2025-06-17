# task2.py
from PIL import Image
import numpy as np
import os
from scipy.ndimage import uniform_filter

def spatial_average(image_path, output_path, kernel_size):
    """
    Apply spatial averaging filter to an image.
    :param image_path: Path to input image
    :param output_path: Path to save output image
    :param kernel_size: Size of the averaging kernel (e.g., 3 for 3x3)
    """
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Apply uniform filter (averaging)
    averaged_array = uniform_filter(img_array, size=kernel_size)
    averaged_array = averaged_array.astype(np.uint8)
    
    # Save output image
    Image.fromarray(averaged_array).save(output_path)
    print(f"Image with {kernel_size}x{kernel_size} averaging saved to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Test with different kernel sizes
    for kernel_size in [3, 10, 20]:
        output_path = os.path.join(output_dir, f"average_{kernel_size}x{kernel_size}.jpg")
        try:
            spatial_average(input_path, output_path, kernel_size)
        except Exception as e:
            print(f"Error for kernel_size={kernel_size}: {e}")

if __name__ == "__main__":
    main()