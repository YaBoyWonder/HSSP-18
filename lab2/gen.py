'''
Generate a training and a test data set.
'''
import json
import random
import numpy as np

loc_1 = -3
loc_2 = 2
scale_1 = 2
scale_2 = 0.5
size = 2000

data_1 = np.random.normal(loc_1, scale_1, size).tolist()
data_2 = np.random.normal(loc_2, scale_2, size).tolist()
training = {'set 1': data_1, 'set 2': data_2}

with open('training.json', 'w') as f:
    json.dump(training, f)

data_1 = np.random.normal(loc_1, scale_1, size).tolist()
data_2 = np.random.normal(loc_2, scale_2, size).tolist()
answer = {'set 1': data_1, 'set 2': data_2}
test = data_1 + data_2
random.shuffle(test)

with open('test.json', 'w') as f:
    json.dump(test, f)


with open('answer.json', 'w') as f:
    json.dump(answer, f)
