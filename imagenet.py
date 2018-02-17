
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from scipy.io import loadmat

data = loadmat("./objects-train.mat")
images = data["images_train"]
print(images[0])
model = VGG16(weights = 'imagenet', include_top = False)



