
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from scipy.io import loadmat
from skimage.transform import resize
data = loadmat("./objects-train.mat")
images = data["images_train"]

images = np.array(images).T

#print(images[0])
#print(np.array(images[0]).shape)

i = images[10]


#print(i.shape)
model = VGG16(weights = 'imagenet',input_shape = (48,48,3),include_top = False)
#print(model)
count = 0
x = []
for i in images:
	count += 1
	if count % 10 == 0:
		print("10 images processed")
	elif count >= 100:
		break 
	i = np.reshape(i,(28,28))
	i = np.dstack((i,i,i))
	i = resize(i,(48,48))

	#i = np.reshape(i,(3,28,28))
	#x = image.img_to_array(i)
	#img = image.load_img('./elephant.jpg', target_size=(224, 224))
	i = image.img_to_array(i)
	x.append(i)

x = np.array(x)

print(x.shape)

x = preprocess_input(x)

#print(x)

features = model.predict(x)

print(features)
print("here")


