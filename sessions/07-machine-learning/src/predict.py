import keras
import random
import matplotlib.pyplot as plt
from train import load_data
from keras.models import load_model



def predict(num_samples, is_fashion=False):
	# Choose random num_samples from test set
	samples = random.sample(list(zip(test_xs, test_ys)), num_samples)

	for sample_x, sample_y in samples:
		# Get model predictions
		sample_x = sample_x.reshape(1, *sample_x.shape)
		predict_label = model.predict_classes(sample_x)[0]
		actual_label = sample_y
		if is_fashion:
			predict_label = mapping[predict_label]
			actual_label = mapping[actual_label]
		print(f'Predicted class: {predict_label}')
		print(f'Actual class: {actual_label}\n')

		# Plot sample image
		pixels = (sample_x * 255).reshape(28, 28)
		plt.title(sample_y)
		plt.imshow(pixels, cmap='gray')
		plt.show()



# Will run only if file is the entry point
# Allows file to be imported without executing below code
if __name__ == '__main__':
	# Mapping for fashion_mnist
	mapping = {
		0: 'T-shirt',
		1: 'Trouser',
		2: 'Pullover',
		3: 'Dress',
		4: 'Coat',
		5: 'Sandal',
		6: 'Shirt',
		7: 'Sneaker',
		8: 'Bag',
		9: 'Ankle boot'
	}
	(train_xs, train_ys), (test_xs, test_ys) = load_data()
	model = load_model('mnist.h5')	# Path to model file
	predict(20)	# Number of samples to predict
	# Set 2nd parameter to True for fashion_mnist