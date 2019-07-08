from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

# Training data directory
good_data_dir = 'training_images'

# Test data
test_data_dir = 'test_images'

# Total samples (below x 2 for good and bad)
training_samples = 222
test_samples = 20


# Define epoch and batch size (what exactly is this?)
epochs = 10
batch_size = 16

# Check to ensure images are correct size (how images are formatted)
img_width = 150
img_height = 70
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
