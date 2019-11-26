import keras
from keras.datasets import mnist, fashion_mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense



def load_data():
	# Load dataset
	(train_xs, train_ys), (test_xs, test_ys) = mnist.load_data()

	# Reshaping the train and test sets
	train_xs = train_xs.reshape(*train_xs.shape, 1)
	test_xs = test_xs.reshape(*test_xs.shape, 1)

	# Casting from int to float values
	train_xs = train_xs.astype('float32')
	test_xs = test_xs.astype('float32')

	# Normalizing the values between 0 and 1
	train_xs = train_xs / 255
	test_xs = test_xs / 255

	return (train_xs, train_ys), (test_xs, test_ys)



def create_model():
	# Create a sequential deep learning model
	model = Sequential()

	# Conv Layer
	model.add(Conv2D(input_shape=(28, 28, 1),
					kernel_size=5,
					filters=8,
					strides=1,
					activation='relu',
					kernel_initializer='VarianceScaling'))
	
	# Pooling layer to halve the output from previous layer
	model.add(MaxPooling2D(pool_size=(2, 2), strides=2))

	# Conv layer
	model.add(Conv2D(kernel_size=5,
					filters=16,
					strides=1,
					activation='relu',
					kernel_initializer='VarianceScaling'))

	# Flatten layer output of the previous layer to a 1D vector
	model.add(Flatten())

	# Fully-Connected Layer
	model.add(Dense(units=128,
					activation='relu',
					kernel_initializer='VarianceScaling'))
	
	# Output layer
	model.add(Dense(units=10,
					activation='softmax',
					kernel_initializer='VarianceScaling'))
	
	# Compile the model
	model.compile(optimizer='adam',
				loss='sparse_categorical_crossentropy',
				metrics=['accuracy'])
	
	return model



def train():
	# Train the model
	model.fit(train_xs, train_ys,
			batch_size=32,
			validation_data=(test_xs, test_ys),
			epochs=12,
			shuffle=True,
			verbose=1)
	
	# Checking how well the model performed
	test_loss, test_accuracy = model.evaluate(test_xs, test_ys, verbose=0)
	print('Test loss:', test_loss)
	print('Test accuracy:', test_accuracy)
	


# Will run only if file is the entry point
# Allows file to be imported without executing below code
if __name__ == '__main__':
	(train_xs, train_ys), (test_xs, test_ys) = load_data()
	model = create_model()
	model.summary()
	train()

	# Save model as 'model.h5' in current directory
	model.save('model.h5')