# cifar10_Inception
**an implementation of Inception architecture on the cifar dataset in tensorflow**

**Aims**
This is my attempt to learn how to optimize time taken to train neural networks, which is the biggest bottleneck in deep learning today. I aim to accomplish this in 2 ways:
* Using a light-weight architecture like inception
* configure all libraries/tools to optimize system usage.

**Backround**
Though the Inception architecture was implemented on the ILSVRC14 dataset which has an average resolution of 400 x 400, the algorithm compresses it to 224 x 224 and most of the Inception modules are implemented on tensors of size 34 x 34 x depth and 17 x 17 x depth.

This suggests that the 32 x 32 x 3 sized cifar dataset may not be too small for this architecture. Anyhow this claim is highly speculative and can only be supported by rigorous trial and error. The code is designed to be as modular as possible with most of the model defined in an accompanying CSV file.

My main motivation for this project is that the dataset is small enough for a CPU only interpretation that I can run on my laptop. The major aim of the Inception architecture is to enable Ml on smaller machines, which is further incentive.

The current state of the art for cifar10 is 96.5 %

#Performance
This model is built on top of the [default cifar CNN](https://github.com/tensorflow/models/tree/master/tutorials/image/cifar10) published by Tensorflow. The following system was used to run this model:
* Nvidia GeForce GTX 1060 GPU
* Intel i5-4440 Processor

**published by tensorflow for default model**
1 Tesla K20m  accuracy: ~86% at 60K steps  (5 hours)
1 Tesla K40m  accuracy: ~86% at 100K steps (4 hours)
These results are obselet as a newer GPU architecture (pascal) is available

**default model using standard configuration on mentioned system**



**guidelines to run locally**
clone this repo with
```shell
git clone https://github.com/praneethmendu/cifarInception.git
```
Run the script [download.py](download.py) to download and extract the datasets or download them from [ Alex Krizhevsky's page](https://www.cs.toronto.edu/~kriz/cifar.html) and extract manually into the main folder.
To perform a check or view some of the datasets images use [print_examples.py](print_examples.py).

Now you can run [hundred.ipynb](hundred.ipynb) and [ten.ipynb](ten.ipynb). Edit [model.csv](model.csv) to change the sizes of individual filers in different inception modules.

To run [Tensorboard](https://www.tensorflow.org/how_tos/summaries_and_tensorboard/) cd to the main folder and run the following code. It can be viewed on any browser at http://127.0.1.1:6006/
```shell
tensorboard --logdir=run1:log --port 6006
```
