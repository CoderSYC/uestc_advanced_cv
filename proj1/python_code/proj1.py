import cv2

# Before trying to construct hybrid images, it is suggested that you
# implement my_imfilter.m and then debug it using proj1_test_filtering.m

# Debugging tip: You can split your MATLAB code into cells using "##"
# comments. The cell containing the cursor has a light yellow background,
# and you can press Ctrl+Enter to run just the code in that cell. This is
# useful when projects get more complex and slow to rerun from scratch

## Setup
# read images and convert to floating point format
from my_imfilter import my_imfilter
from utils import luo_imshow, luo_imwrite, luo_fspecial
from vis_hybrid_image import vis_hybrid_image

image1 = cv2.imread('../data/einstein.bmp')
image2 = cv2.imread('../data/marilyn.bmp')

# Several additional test cases are provided for you, but feel free to make
# your own (you'll need to align the images in a photo editor such as
# Photoshop). The hybrid images will differ depending on which image you
# assign as image1 (which will provide the low frequencies) and which image
# you asign as image2 (which will provide the high frequencies)

## Filtering and Hybrid Image construction
cutoff_frequency = 7  # This is the standard deviation, in pixels, of the
# Gaussian blur that will remove the high frequencies from one image and
# remove the low frequencies from another image (by subtracting a blurred
# version from the original version). You will want to tune this for every
# image pair to get the best results.

filter = luo_fspecial(cutoff_frequency * 4 + 1, cutoff_frequency * 4 + 1, cutoff_frequency)
###################################################################
# YOUR CODE BELOW. Use my_imfilter create 'low_frequencies' and
# 'high_frequencies' and then combine them to create 'hybrid_image'
###################################################################

########################################################################
# Remove the high frequencies from image1 by blurring it. The amount of
# blur that works best will vary with different image pairs
########################################################################

low_frequencies = my_imfilter(image1, filter)

########################################################################
# Remove the low frequencies from image2. The easiest way to do this is to
# subtract a blurred version of image2 from the original version of image2.
# This will give you an image centered at zero with negative values.
########################################################################

high_frequencies = image2 - my_imfilter(image2, filter)

########################################################################
# Combine the high frequencies and low frequencies
########################################################################

hybrid_image = low_frequencies + high_frequencies

## Visualize and save outputs
luo_imshow("low", low_frequencies)
luo_imshow("high", high_frequencies)
luo_imshow("vis_hybrid_image", hybrid_image)
vis = vis_hybrid_image(hybrid_image)
luo_imshow("vis", vis)
luo_imwrite(low_frequencies, "low_frequencies.jpg")
luo_imwrite(high_frequencies, "high_frequencies.jpg")
luo_imwrite(hybrid_image, "hybrid_image.jpg")
luo_imwrite(vis, "vis.jpg")

import time

time.sleep(100)
