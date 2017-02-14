import numpy as np
import _pickle
import png

with open('cifar-100-python/train', 'rb') as f1:
    dict = _pickle.load( f1 , encoding='latin1')
    predata = dict['data']
    labels = dict['fine_labels']
    
with open('cifar-100-python/test', 'rb') as f2:
    dict = _pickle.load( f2 , encoding='latin1')
    preval_data = dict['data'][:5000]
    val_labels = dict['fine_labels'][:5000]
    pretest_data = dict['data'][5000:]
    test_labels = dict['fine_labels'][5000:]

with open('cifar-100-python/meta', 'rb') as f3:
    dict = _pickle.load( f3 , encoding='latin1')
    names=dict['fine_label_names']

del dict


def fit(arr):
    p = arr.reshape((-1, 3, 32 ,32))
    p = p.swapaxes(1,3)
    p = p.swapaxes(1,2)
    return p

predata = fit(predata)
preval_data = fit(preval_data)
pretest_data = fit(pretest_data)

# choose numbers to print

numbers_to_print = [1598,13]

for num in numbers_to_print :
    
    f = open(str(num) + '_' + names[labels[num]] +'.png', 'wb')      # binary mode is important
    w = png.Writer(32,32)
    w.write(f, np.reshape(predata[num], (-1, 96)))
    f.close()
