from keras.preprocessing.image import ImageDataGenerator
#Generating new images from existing images
#train_datagen=ImageDataGenerator(rotation_range=60,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest',rescale=1./255)

train_datagen=ImageDataGenerator(shear_range=0.2,zoom_range=0.2,horizontal_flip=True,rescale=1./255)#next try no fill mode

#class_list=['Paper','Scissors','Stone']
test_datagen = ImageDataGenerator(rescale=1./255)
valid_datagen= ImageDataGenerator(rescale=1./255)

def Train():
    train_set=train_datagen.flow_from_directory('Operation2/Train',target_size=(150,150),color_mode="grayscale",batch_size=16,shuffle=True,class_mode='sparse',seed=7) #class_mode="categorical" for 2d onehot encoded labels
    return train_set

def Valid():
  valid_set = valid_datagen.flow_from_directory('Operation2/Valid',target_size=(150,150),color_mode="grayscale",batch_size=16,shuffle=True,class_mode='sparse',seed=13) #class_mode="categorical" for 2d onehot encoded labels
  return valid_set

def Test():
   test_set = test_datagen.flow_from_directory('Operation2/Test',target_size=(150, 150),color_mode="grayscale",batch_size=16,shuffle=True,class_mode='sparse',seed=78) #class_mode="categorical" for 2d onehot encoded labels
   return test_set


#Train=Train()
#Test=Test()

#print(Train.class_indices)

#fruit_indices=Train.class_indices


#print(type(train_generator))
#print(type(test_datagen))
#print(type(datagen))

#a=Train()
'''img=load_img('A0.jpg')
x=img_to_array(img)
x=x.reshape((1,)+x.shape)
#print(x.shape)

i=0
for batch in datagen.flow(x,batch_size=1,save_to_dir='preview2',save_prefix='el',save_format='png'):
    i+=1
    if i>20:
        break
'''