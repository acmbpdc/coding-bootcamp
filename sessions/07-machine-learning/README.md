# Machine Learning

## Motivation

### What is Machine Learning?

Machine learning is the science of getting computers to act without being explicity programmed. It is an application of Artificial Intelligence with the primary aim to allow computers to learn automatically without human intervention.

### Why should you learn ML?

*   #### Data is power.
    
    Harnessing the power of data gives you extreme power. All organizations are racing to use data to reshape their technology and business. However, few people actually have the skills to use data in the right way.

*   #### ML is linked directly to data science.

    ML career helps you to become competent in both the fields. It means you can analyse data, preprocess and get insights, and use results to train an ML model to predict results.

*   #### The pay is let's say amazing.

    The average machine learning engineer earns close to $121,000 according to [glassdoor](https://www.glassdoor.com/Salaries/machine-learning-engineer-salary-SRCH_KO0,25.htm).

*   #### It can be daunting at first but it's a lot of fun.

    AI is transforming the way we live today. Being part of this change and contributing by building exciting applications is a lot of fun! It also makes you look hella cool.

## Introduction

We'll build a model to recognize hardwritten digits with a convolutional neural network. First, we'll train the model by having it _look_ at thousands of handwritten digits with their corresponding labels. Then, we'll evaluate how well our model performs by using test images that the model has never seen.

The task at hand is known as classification as we are trying to classify a number ranging from 0 to 9 for a given handwritten image. We train the model by showing it many input images along with their corresponding label, this is known as supervised learning.

To build deep learning models, we have many frameworks that contain most of the code to handle the underlying intricacies. One such popular framework is Keras written in python that we will be using today. It focuses on being user-friendly, modular and extensible. In addition, to enhance the efficiency and give more control, Keras can work on top of TensorFlow which is highly used in production level models. In essence, we will be writing our code in Keras and execute it with the help of TensorFlow's functionality.

Let's start by importing `keras`

```python
import keras
```

## Load Data

We will be using the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. This dataset contains a training set of 60,000 examples and a test set of 10,000 examples. It is a good dataset for beginners to create their first model.

>   #### The MNIST Database
>
>   MNIST is an acronym that stands for the Modified National Institute Of Standards and Technology. One of the researchers is Yann LeCun who is now the VP and Chief AI scientist at Facebook.

![](assets/mnist.png)

Above image contains samples from the dataset. Each image is 28px wide 28px high and has 1 color channel as it is in grayscale (0-255). There are 60,000 train images and 10,000 test images. Hence, the shape of training set is `[60000, 28, 28, 1]` and the shape of test set is `[10000, 28, 28, 1]`.

>   #### Color Channels
>
>   Grayscale images have a single color channel ranging from 0 to 255 giving us black and white images. There are different types of color images:
>
>   *   RGB - 3 channels: red, green, and blue
>   *   HSV - 3 channels: hue, saturation, value
>   *   CMYK - 4 channels: cyan, magenta, yellow, and black
>
>   Color images have a different input shape. For example, if we had an RGB image meaning 3 color channels, the train set shape would change to  `[60000, 28, 28, 3]`. You can learn more about color channels on [this](https://en.wikipedia.org/wiki/Channel_(digital_image) wikipedia page.

Our goal is to train a model that will take one input image and predict a score for each of the 10 possible classes that the image may belong to, the 10 classes represent the digits 0 to 9 inclusively. Keras contains many of the popular datasets which are present `keras.datasets`, the entire list can be found [here](https://keras.io/datasets/).

Let's import the mnist dataset

```python
from keras.datasets import mnist

# Load dataset
(train_xs, train_ys), (test_xs, test_ys) = mnist.load_data()
```

Keras returns a tuple for the train and test sets. We can use tuple unpacking to store them separately. Each of these sets contain the handwritten images and the labels, hence we can use tuple unpacking again to extract them.

Let's check the shape of the `xs`

```python
print(train_xs.shape)   # (60000, 28, 28)
print(test_xs.shape)    # (10000, 28, 28)
```

We see the shape is `[60000, 28, 28]` for the train set. However, we need an extra dimension for the grayscale color channel and there are two ways to do this

```python
# Reshaping the train and test sets
train_xs = train_xs.reshape(*train_xs.shape, 1) # same as train_xs.reshape(60000, 28, 28, 1)
test_xs = test_xs.reshape(*test_xs.shape, 1)    # same as test_xs.reshape(10000, 28, 28, 1)
```

The images are in the grayscale format ranging from 0 to 255. It is a good idea to normalize the images to a scale of 0 to 1, we can do it by just dividing the `xs` by `255`

```python
# Normalizing the values between 0 and 1
train_xs = train_xs / 255
test_xs = test_xs / 255
```

Sometimes you might get an error since you are trying to divide an `int` and get a `float` result. You can confirm this by printing the data type of the `xs` before the division

```python
print(train_xs.dtype)   # uint8
print(test_xs.dtype)    # uint8
```

A safer way is to cast the `xs` into a `float` value before you do the divison

```python
# Casting from int to float values
train_xs = train_xs.astype('float32')
test_xs = test_xs.astype('float32')

# Normalizing the values between 0 and 1
train_xs = train_xs / 255
test_xs = test_xs / 255
```

## Model Architecture

There are two ways to create a model in Keras:

*   `Sequential`: Allows you to create a layer-by-layer model. It is called sequential because its inputs flow straight down to its output.
*   `Functional`: Gives a lot more flexibility by allowing to create models that do more than just connect to the previous and next layers. You can connect a layer to any other layer giving you much more complex networks.

These are present in `keras.models`. We don't need to create any complex networks and hence we will create a `Sequential` model

```python
from keras.models import Sequential

model = Sequential()
```

Keras gives you a wide range of layers to choose from depending on your application all of which are present in `keras.layers`. We need to include these imports

```python
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
```

Next we define our layers. Each layer in our network tries to build onto the work extracted from the previous layer.

>   #### Goal of Layers
>
>   Layers extract useful information from the data fed into them. The goal is to have meaningful representations for our problem. 
>   Take a problem of recognizing parts of a human face from a selfie. The first layer may extract the person from the background. The second layer may extract parts of the human body from the person such as the arms, legs, face and so on. The third layer may extract parts of the face itself like the eyes, nose, mouth, hair and ears. The fourth layer may extract more in depth features such as the wrinkles, dark circles, dimples and more.

The first layer in our model is the Convolutional Layer. This layer acts as the eyes of our neural network, in other words, it allows our model to see

```python
# Conv Layer
model.add(Conv2D(input_shape=(28, 28, 1),
                 kernel_size=5,
                 filters=8,
                 strides=1,
                 activation='relu',
                 kernel_initializer='VarianceScaling'))
```

>   #### Activation Function
>
>   The activation function is used to transform the output of the layer. Essentially, it decides if the neuron fires (activates) or not. This "firing" is related with the importance of a feature in affecting the overall output.

Working on large images can be a problem. Take a high resolution color image of 1080px wide 720px high. Since it is an RGB image the total number of parameters is 1080×720×3 = 2,332,800 parameters just for the input image alone! As you keep adding layers, the number of parameters goes on increasing. It is recommended not to exceed 10 million parameters for the entire model as this can have computation as well as other issues (like overfitting).

A resolve to decrease the number of parameters is a technique called pooling. Pooling layers allow us to downsample our feature map by summarizing the features. Two common pooling methods are average pooling and max pooling which summarize by averaging the values in the feature map and choosing the highest activated feature respectively.

```python
# Pooling layer to halve the output from previous layer
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
```

A common practice is to use the same architecture a few times to keep extracting more and more useful information

```python
# Conv layer
model.add(Conv2D(kernel_size=5,
                 filters=16,
                 strides=1,
                 activation='relu',
                 kernel_initializer='VarianceScaling'))
```

Now we are coming close to the final layers of our model. Before passing the output from the conv layers, it's generally a good practice to flatten it. This is because dense layers as we will see later generally take 1D arrays. The flatten layer does exactly this, unrolls our output to one long one-dimensional array.

```python
# Flatten layer output of the previous layer to a 1D vector
model.add(Flatten())
```

The conv layers are used to extract the features from our data. However, our goal is use these features to figure the class label. This is where we use _fully-connected_ layers.

![](assets/fully-connected-layer.png)

They help to link the features together and predict the class label of our data. This is equivalent to the `Dense` layer in Keras.

```python
# Fully-Connected Layer
model.add(Dense(units=128,
				activation='relu',
				kernel_initializer='VarianceScaling'))
```

Finally, we have come to our output layer. For this, we will use a dense layer with softmax activation. The number of units we have is the number of classes, which in our case is 10. Keep in mind we use an activation to compute a probability distribution with confidence scores for each of our 10 classes. The class with the highest score will be the predicted digit.

>   #### Softmax Activation
>
>   The softmax activation gives a probability distribution meaning all the values sum to one. Softmax does something extra too, it pushes a score close to 1 if it is large and a score close to 0 if it is small.

```python
# Output layer
model.add(Dense(units=10,
                activation='softmax',
                kernel_initializer='VarianceScaling'))
```

That completes our model architecture. But wait, we aren't done just yet! Before our model is ready to be trained, it still needs a few more adjustments. This is done at the model's compile step:

*   Loss function: Measures how accurate our model is during training. 
*   Optimizer: Decides on how the model gets updated based on the loss value. Choosing the right function is important as it plays a key role in updating the weights of our model.
*   Metrics: Help in monitoring how well the model is performing. We will use accuracy, the number of correct images classified out of the total images from the validation set.
<!-- *   Learning Rate: Controls how fast or slow the optimizer updates the model. A value too small may take our model a long time to learn. Conversely, a value too large updates our model too quickly making it unstable. -->

```python
# Compile the model
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
```

We can summarize the model and get useful information about:

*   Model architecture including the layers and their order
*   The output shape of each layer
*   The number of parameters in each layer
*   The total number of parameters in the model

```python
model.summary()
```

## Train Model


To train the model, we call `model.fit` method—so called because it _fits_ the models to the training data. Before that, we need to define a few parameters:

*   `batch_size`: Number of training examples present in a single batch. We cannot pass the entire dataset at once so we divide it into a number of batches of reasonable size.
*   `epochs`: Number of times to go through the training set. One epoch is defined as one forward & backward pass over the entire training set. Since one epoch is too big to feed the network at once we divide it into several smaller batches.
*   `shuffle`: bool, shuffle the training data if set to `True`.
*   `verbose`: int, 0 &rarr; silent, 1 &rarr; progress bar, 2 &rarr; one line per epoch.
*   `validation_data`: data to evaluate the model during training, helps in tuning the model configuration.

```python
# Train the model
model.fit(train_xs, train_ys,
          batch_size=32,
          validation_data=(test_xs, test_ys),
          epochs=12,
          shuffle=True,
          verbose=1)
```

Now we evaluate the accuracy of our model on the test dataset, i.e., data that it has never seen.

>   #### Validation set vs. Test set
>
>   Validation set helps in assessing the model during 
>   In our case, during the training the validation dataset was the test dataset itself. Hence, the accuracy we get during evaluation will be the same as the model accuracy during the training process.

```python
# Checking how well the model performed
test_loss, test_accuracy = model.evaluate(test_xs, test_ys, verbose=0)
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy)
```

## Save & Load Model

Training time can be massive from minutes, hours, and even days. Due to this, it is important to save the trained model properly once it is done. Fortunately, Keras makes this task extremely simple and you just need a single line of code specifying the filename

```python
# Save model as 'model.h5' in current directory
model.save('model.h5')
```

This will save the model weights and architecture into a single file.

>   #### .H5 File
>
>   An H5 file saves data in the Hierarchical Data Format (HDF). This file format is designed to store and organize large amounts of data. This is the reason Keras uses the `HDF5`/`H5` file format to store the model data.

We have now saved the model, but how do we load it? Keras has a module `keras.models` which contains a function for our requirement

```python
from keras.models import load_model

# Load saved model
model = load_model('model.h5')
```

We call `load_model` by passing the filename or path to our saved model file. The function then returns the model with the same weights and architecture.

We can summarize the model to confirm the architecture and evaluate it to confirm the weights are same as our saved model

```python
model.summary()
```

## Code Modularity

Modularity is the concept of breaking a system into separate independent components. It's generally nice to separate the different parts of our project as it helps to avoid clutter and makes our code look cleaner. It also helps for future improvements as we can work on individual components themselves instead of being confused with a mess of codebase.

Add the code from each part to the following functions

```python
def load_data():
    # Code for Load Data
    return (train_xs, train_ys), (test_xs, test_ys)

def create_model():
    # Code for Model Architecture
    return model

def train():
    # Code for Train Model

(train_xs, train_ys), (test_xs, test_ys) = load_data()
model = create_model()
train()

# Save model as 'model.h5' in current directory
model.save('model.h5')
```

## Summary

We covered:

*   [Motivation](#motivation)
*   [Introduction](#introduction)
*   [Load Data](#load-data)
*   [Model Architecture](#model-architecture)
*   [Train Model](#train-model)
*   [Save & Load Model](#save-&-load-model)