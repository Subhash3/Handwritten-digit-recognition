#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('pip3 install neuralnetworks-shine7')


# In[20]:


# Import Required Libraries
from Model import NeuralNetwork
# from Model import Dataset
# import mnist
import numpy as np

from matplotlib import pyplot as plt


# In[18]:


# Display a gray scale visualisation of the input(image) vector
def showImage(input_vector) :
    image = np.reshape(input_vector, (28, 28))

    plt.imshow(image, cmap='gray')
    plt.show()


# In[19]:


# Parse the filename containing training data
def parsefile(filename, msg="") :
    dataset = list()
    print("Preparing " + msg + " Dataset....")
    label_and_pixels = open(train_file).readlines()
    i = 0
    for line in label_and_pixels :
        target = [0]*outputs
        data_vector = list(map(int, line.split(',')))
        input_vector = data_vector[1:785]
        label = data_vector[0]
        target[label] = 1
        
        sample = list()
        sample.append(np.reshape(input_vector, (784, 1)))
        sample.append(np.reshape(target, (10, 1)))
        dataset.append(sample)

    print("Done!")
    return dataset


# In[6]:


# Training data file
# You can also use mnist package of python
train_file = "./datasets/MNIST/train.csv"

inputs = 784 # 28 x 28 images
outputs = 10 # 0 to 9
dataset = parsefile(train_file, "Training")


# In[21]:


brain = NeuralNetwork(inputs, outputs) # Create a neural network
brain.addLayer(16, activation_function="tanh") # Hidden layer with 16 neurons
brain.compile(activation_function="sigmoid") # Finish the network by adding output layer


# In[9]:


# The dataset contains 42000 data samples.
# Using the first 1000 for training.
size = 1000
# One has to train with all the (42k) datasamples and testing it with a seperate testing file for better accuracy

# Train the network(brain) for 2000 epochs. (Increase for better accuracy)
brain.Train(dataset[:size], size, epochs=2000, logging=False)


# In[10]:


# Check the accuracy

brain.evaluate()


# In[22]:


# Testing with the next 20 samples.
for i in range(size, size+20) :
    test = dataset[i]
    output = brain.predict(test[0])
    showImage(test[0])
    m = max(output[0].tolist())
    index = output[0].tolist().index(m)
    # print(output)
    print("It is a:", index)


# In[32]:


# Export the model if you want to.

filename = "new_model.json"

brain.export_model(filename)


# In[ ]:


# Load an exported model

new_brain = NeuralNetwork.load_model("handwritten_digits.json")
# If you want to train it further, train the new_brain since it has already been trained for 2000 epochs.

