import tensorflow as tf
from tensorflow import keras
import os

label = ['Shirts', 'Jeans', 'Watches', 'Track Pants', 'Tshirts', 'Socks', 'Casual Shoes',
 'Belts', 'Flip Flops', 'Handbags', 'Tops', 'Bra', 'Sandals', 'Shoe Accessories',
 'Sweatshirts', 'Deodorant', 'Formal Shoes', 'Bracelet', 'Lipstick', 'Flats',
 'Kurtas', 'Waistcoat', 'Sports Shoes', 'Shorts', 'Briefs', 'Sarees',
 'Perfume and Body Mist', 'Heels', 'Sunglasses', 'Innerwear Vests', 'Pendant',
 'Laptop Bag', 'Scarves', 'Dresses', 'Night suits', 'Skirts', 'Wallets',
 'Blazers', 'Ring', 'Kurta Sets', 'Clutches', 'Shrug', 'Backpacks', 'Caps',
 'Trousers', 'Earrings', 'Camisoles', 'Boxers', 'Jewellery Set', 'Dupatta',
 'Capris', 'Lip Gloss', 'Bath Robe', 'Mufflers', 'Tunics', 'Jackets', 'Trunk',
 'Lounge Pants', 'Face Wash and Cleanser', 'Necklace and Chains',
 'Duffel Bag', 'Sports Sandals', 'Foundation and Primer', 'Sweaters',
 'Free Gifts', 'Trolley Bag', 'Tracksuits', 'Swimwear', 'Shoe Laces',
 'Fragrance Gift Set', 'Bangle', 'Nightdress', 'Ties', 'Baby Dolls', 'Leggings',
 'Highlighter and Blush', 'Travel Accessory', 'Kurtis', 'Mobile Pouch',
 'Messenger Bag', 'Lip Care', 'Nail Polish', 'Eye Cream', 'Accessory Gift Set',
 'Beauty Accessory', 'Jumpsuit', 'Kajal and Eyeliner', 'Water Bottle',
 'Suspenders', 'Face Moisturisers', 'Lip Liner', 'Robe', 'Salwar and Dupatta',
 'Patiala', 'Stockings', 'Eyeshadow', 'Headband', 'Tights', 'Nail Essentials',
 'Churidar', 'Lounge Tshirts', 'Face Scrub and Exfoliator', 'Lounge Shorts',
 'Gloves', 'Wristbands', 'Tablet Sleeve','Ties and Cufflinks', 'Footballs',
 'Compact', 'Stoles', 'Shapewear', 'Nehru Jackets', 'Salwar', 'Cufflinks', 'Jeggings', 'Hair Colour', 'Concealer', 'Rompers', 'Sunscreen'
,'Booties','Mask and Peel', 'Waist Pouch', 'Hair Accessory', 'Body Lotion', 'Rucksacks',
 'Basketballs', 'Lehenga Choli', 'Clothing Set', 'Mascara', 'Cushion Covers',
 'Key chain', 'Rain Jacket', 'Toner', 'Lip Plumper', 'Umbrellas',
 'Face Serum and Gel', 'Hat', 'Mens Grooming Kit', 'Makeup Remover',
 'Body Wash and Scrub', 'Suits', 'Ipad']

def make_directory(target_path):
  if not os.path.exists(target_path):
    os.mkdir(target_path)
    print('Directory ', target_path, ' Created ')
  else:
    print('Directory ', target_path, ' already exists')

print('TensorFlow version: {}'.format(tf.__version__))

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# reshape for feeding into the model
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print('\ntrain_images.shape: {}, of {}'.format(train_images.shape, train_images.dtype))
print('test_images.shape: {}, of {}'.format(test_images.shape, test_images.dtype))

model = keras.Sequential([
  keras.layers.Conv2D(input_shape=(28,28,1), filters=8, kernel_size=3, 
                      strides=2, activation='relu', name='Conv1'),
  keras.layers.Flatten(),
  keras.layers.Dense(10, activation=tf.nn.softmax, name='Softmax')
])
model.summary()

epochs = 5

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=epochs)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\nTest accuracy: {}'.format(test_acc))

# Fetch the Keras session and save the model
# The signature definition is defined by the input and output tensors,
# and stored with the default serving key
SAVED_MODEL_PATH = './saved_model'
make_directory(SAVED_MODEL_PATH)
MODEL_DIR = SAVED_MODEL_PATH

version = 1
export_path = os.path.join(MODEL_DIR, str(version))
print('export_path = {}\n'.format(export_path))

tf.keras.models.save_model(
  model,
  export_path,
  overwrite=True,
  include_optimizer=True,
  save_format=None,
  signatures=None,
  options=None
)
print('\nSaved model:')
