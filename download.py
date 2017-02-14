import urllib.request
import tarfile
import os

def cif10():
    urllib.request.urlretrieve("https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz", "cifar-10-python.tar.gz")

    tar = tarfile.open(cifar-10-python, "r:gz")
    tar.extractall()
    tar.close()
    os.remove("cifar-10-python.tar.gz")

def cif100():
    urllib.request.urlretrieve("https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz", "cifar-10-python.tar.gz")

    tar = tarfile.open(cifar-100-python, "r:gz")
    tar.extractall()
    tar.close()
    os.remove("cifar-100-python.tar.gz")
    
choice = input("Choose Download :\ncifar10[1] \ncifar100[2] \nboth[3]\n")
 
if choice == 1: cif10()
if choice == 2: cif10()
if choice == 3: 
    cif10()
    cif100()
