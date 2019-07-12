import numpy as np
from keras.models import load_model
from ImgPrepro import Valid,Train,Test
import matplotlib.pyplot as plt
from keras.preprocessing import image
import pandas as pd
import cv2
model=load_model('SegmentationSimplbgrnd.h5')


valid=Valid()
acc=model.evaluate_generator(generator=valid,pickle_safe=False)
print("Accuracy:",acc[1])