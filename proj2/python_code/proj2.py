# Local Feature Stencil Code
# CS 143 Computater Vision, Brown U.
# Written by James Hays
import cv2
import numpy as np

# This script
# (1) Loads and resizes images
# (2) Finds interest points in those images                 (you code this)
# (3) Describes each interest point with a local feature    (you code this)
# (4) Finds matching features                               (you code this)
# (5) Visualizes the matches
# (6) Evaluates the matches based on ground truth correspondences

# There are numerous other image sets in /course/cs143/asgn/proj2/data/
# You can simply download images off the Internet, as well. However, the
# evaluation function at the bottom of this script will only work for this
# particular image pair (unless you add ground truth annotations for other
# image pairs). It is suggested that you only work with these two images
# until you are satisfied with your implementation and ready to test on
# additional images. A single scale pipeline works fine for these two
# images (and will give you full credit for this project), but you will
# need local features at multiple scales to handle harder cases.
from get_interest_points import get_interest_points

image1 = cv2.imread('../data/Notre Dame/921919841_a30df938f2_o.jpg')
image2 = cv2.imread('../data/Notre Dame/4191453057_c86028ce1f_o.jpg')

# You don't have to work with grayscale images. Matching with color
# information might be helpful.

# You don't have to work with grayscale images. Matching with color
# information might be helpful.
image1 = cv2.cvtColor(image1.astype('float32') / 255, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2.astype('float32') / 255, cv2.COLOR_BGR2GRAY)

scale_factor = 0.5  # make images smaller to speed up the algorithm
image1 = cv2.resize(image1, None, fx=scale_factor, fy=scale_factor)
image2 = cv2.resize(image2, None, fx=scale_factor, fy=scale_factor)

feature_width = 16  # width and height of each local feature, in pixels.

## Find distinctive points in each image. Szeliski 4.1.1
# !!! You will need to implement get_interest_points. !!!
x1, y1 = get_interest_points(image1, feature_width)
x2, y2 = get_interest_points(image2, feature_width)