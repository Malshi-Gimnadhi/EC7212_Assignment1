# task1.py
from PIL import Image
import numpy as np
import os

def reduce_intensity_levels(image_path, output_path, levels):
    
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Validate levels (must be power of 2)
    if not (levels > 0 and (levels & (levels - 1)) == 0):
        raise ValueError("Number of levels must be a power of 2")
    
    # Normalize to [0, 1], quantize, and scale back to [0, 255]
    img_array = img_array / 255.0
    img_array = np.floor(img_array * (levels - 1)) / (levels - 1) * 255
    img_array = img_array.astype(np.uint8)
    
    # Save output image
    Image.fromarray(img_array).save(output_path)
    print(f"Image with {levels} intensity levels saved to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Test with different intensity levels
    for levels in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
        output_path = os.path.join(output_dir, f"intensity_{levels}.jpg")
        try:
            reduce_intensity_levels(input_path, output_path, levels)
        except Exception as e:
            print(f"Error for levels={levels}: {e}")

if __name__ == "__main__":
    main()