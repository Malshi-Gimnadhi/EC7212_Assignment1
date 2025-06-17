
# EC7212 – Computer Vision and Image Processing
## Take Home Assignment 1
This report details the implementation of various image processing techniques using Python. 
The operations include reducing intensity levels, applying spatial average filters, rotating 
images, and performing block-wise average down sampling. These techniques are applied to 
analyze and manipulate a sample image, with results visualized and saved for comparison.

### Methodology
The image processing tasks were performed using the OpenCV library for image manipulation 
and Matplotlib for visualization. The methodology involved: 
• Loading the image in grayscale and color formats. 
• Implementing functions for intensity level reduction, spatial averaging, image rotation, 
and block-wise averaging. 
• Processing the image with varying parameters like intensity levels, kernel sizes, block 
sizes. 
• Saving the processed images in designated output folders for analysis.


This repository contains Python programs for image processing tasks:
1. Reduce intensity levels to powers of 2.
2. Apply spatial averaging with 3x3, 10x10, and 20x20 kernels.
3. Rotate image by 45 and 90 degrees.
4. Block averaging with 3x3, 5x5, and 7x7 blocks.

### Requirements
- Python 3.x
- Libraries: Pillow, numpy, scipy
- Install: `pip install Pillow numpy scipy`
