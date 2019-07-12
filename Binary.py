from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint

path1='Operation2/BPTrain/New/a.jpg'
path2='Operation2/BPTrain/new.jpg'

inp_image = imread(path1)
img_gray = rgb2gray(inp_image)

thresh = threshold_otsu(img_gray)
binary_thresh_img = img_gray >thresh

imsave(path2, img_as_uint(binary_thresh_img))