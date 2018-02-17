from scipy.io import loadmat
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.cluster import supervised
from scipy.optimize import linear_sum_assignment

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from skimage.transform import resize

# data = loadmat('../digits/digits-train.mat')

data = loadmat('../objects/objects-train.mat')
labels = np.array(data['labels_train']).flatten()
#labels = labels[:100]
fea_hog = np.array(data['fea_hog_train'])

fea_scat = np.array(data['fea_scat_train'])
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
	# count += 1
	# if count % 10 == 0:
	# 	print("10 images processed")
	# elif count >= 100:
	# 	break
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

#labels = np.array(data['labels_train']).flatten()

print(features.shape)
features = features.squeeze(axis=(1,2))
print(features.shape)
#features = np.append(features, )
#print(fea_hog.transpose().shape)

kmeans = KMeans(n_clusters=5).fit(features)

labels_pred = np.array(kmeans.labels_)

print(labels_pred.shape)
print(labels.shape)

labels, labels_pred = supervised.check_clusterings(labels, labels_pred)
# labels_true : int array with ground truth labels, shape = [n_samples]
# labels_pred : int array with estimated labels, shape = [n_samples]
value = supervised.contingency_matrix(labels, labels_pred)
# value : array of shape [n, n] whose (i, j)-th entry is the number of samples in true class i and in predicted class j
[r, c] = linear_sum_assignment(-value)
accr = value[r, c].sum() / len(labels)

print(accr)

# for x in range(0,20):
#     print(kmeans.labels_[x])

# for x in range(0,10):
#     print(data['fea_hog_train'][x])
