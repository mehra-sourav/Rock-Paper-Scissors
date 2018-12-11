from keras import backend as K
from keras.models import load_model
import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential

layer_num=3
filter_num=0
model=load_model('EMode10epoch,6convu6464finalconvu1024denseneurons,2310imgsrmsproplowdataugrescaleintrain.h5')

test_img=cv2.imread('Operation3/Good/live.jpg')
test_img=cv2.resize(test_img,(200,200))
test_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
test_img=np.array(test_img)
test_img=test_img.astype('float32')
test_img/=255
print(test_img.shape)

test_img=np.expand_dims(test_img,axis=0)
test_img=np.expand_dims(test_img,axis=3)
print(test_img.shape)

print(model.predict(test_img))
print(model.predict_classes(test_img))

def featuremaps(model,layerno,X_batch):
    get_activations=K.function([model.layers[0].input,K.learning_phase()],[model.layers[layerno].output,])
    activation=get_activations([X_batch,0])
    return activation

activations=featuremaps(model,layer_num,test_img)

print(np.shape(activations))
feature_maps=activations[0][0]
#print(np.shape(feature_maps))
print(feature_maps.shape)


fig=plt.figure(figsize=(16,16))
plt.imshow(feature_maps[:,:,filter_num])
plt.savefig("Featuremaps-Layer-{}".format(layer_num)+"-filternum-{}".format(filter_num)+'.jpg')

num_of_featuremaps=feature_maps.shape[2]
fig=plt.figure(figsize=(16,16))
plt.title("Featuremaps-layer-{}".format(layer_num))
subplot_num=int(np.ceil(np.sqrt(num_of_featuremaps)))
for i in range(int(num_of_featuremaps)):
    ax=fig.add_subplot(subplot_num,subplot_num,i+1)
    #ax.imshow(output_image[0,:,:,i],interpolation='nearest' ) #to see the first filter
    ax.imshow(feature_maps[:,:,i])
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
plt.show()

fig.savefig("Featuremaps-layer-{}".format(layer_num)+'.jpg')

#score=model.evaluate(,,verbose=0)