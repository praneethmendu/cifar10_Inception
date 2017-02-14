# cifarInception

**an implementation of Inception architecture on the cifar dataset in tensorflow**

Though the Inception architecture was implemented on the ILSVRC14 dataset which has an average resolution of 400 x 400, the algorithm compresses it to 224 x 224 and most of the Inception modules are implemented on tensors of size 34 x 34 x depth and 17 x 17 x depth.

This suggests that the 32 x 32 x 3 sized cifar dataset may not be too small for this architecture. Anyhow this claim is highly speculative and can only be supported by rigorous trial and error. The code is designed to be as modular as possible with most of the model defined in an accompanying CSV file.

My main motivation for this project is that the dataset is small enough for a CPU only interpretation that I can run on my laptop. The major aim of the Inception architecture is to enable Ml on smaller machines, which is further incentive.

The current state of the art for cifar100 is 75.7 %
and for cifar10 it is 96.5 %

# guidelines to run locally
clone this repo with
```shell
git clone https://github.com/praneethmendu/cifarInception.git
```
Run the script [download.py](download.py) to download and extract the datasets or download them from [ Alex Krizhevsky's page](https://www.cs.toronto.edu/~kriz/cifar.html) and extract manually into the main folder.
To perform a check or view some of the datasets images use (print_examples.py)[print_examples.py].

Now you can run [hundred.ipynb](hundred.ipynb) and [ten.ipynb](ten.ipynb). Edit [model.csv](model.csv) to change the sizes of individual filers in different inception modules.

To run [Tensorboard](https://www.tensorflow.org/how_tos/summaries_and_tensorboard/) cd to the main folder and run the following code. It can be viewed on any browser at http://127.0.1.1:6006/
```shell
tensorboard --logdir=run1:log --port 6006
```
