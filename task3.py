# task3.py
from PIL import Image
import os

def rotate_image(image_path, output_path, angle):
    """
    Rotate an image by a specified angle.
    :param image_path: Path to input image
    :param output_path: Path to save output image
    :param angle: Rotation angle in degrees
    """
    # Load image
    img = Image.open(image_path)
    
    # Rotate image
    rotated_img = img.rotate(angle, expand=True)  # expand=True to avoid cropping
    
    # Save output image
    rotated_img.save(output_path)
    print(f"Image rotated by {angle} degrees saved to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Test with different angles
    for angle in [45, 90]:
        output_path = os.path.join(output_dir, f"rotated_{angle}.jpg")
        try:
            rotate_image(input_path, output_path, angle)
        except Exception as e:
            print(f"Error for angle={angle}: {e}")

if __name__ == "__main__":
    main()