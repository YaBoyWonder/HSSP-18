
import math
import json
import matplotlib.pyplot as plt
from matplotlib import colors

plot = True

def load_data():
    with open('training.json', 'r') as f:
        data = json.load(f)
    return (data['set 1'], data['set 2'])

(set_1, set_2) = load_data()

def classify(point):
    closet_1 = 0
    closet_2 = 0
    for p in range(len(set_1)):
        if abs(set_1[p]-point) < abs(set_1[closet_1] - point):
                closet_1 = p

    for p in range(len(set_2)):
        if abs(set_2[p]-point) < abs(set_2[closet_2] - point):
                closet_2 = p

    if abs(point-set_1[closet_1]) < abs(point-set_2[closet_2]):
            return 'A'
    else:
            return 'B'

def check_error(sep):
    error=1

    for point in set_1:
        if point< sep:
            error+=1

    for point in set_2:
        if point > sep:
            error+=1
    return error/len(total_points)

for i in range(100000):
    candidate_1= s+ s_d
    candidate_2= s - s_d

    if check_error(candidate_1)<check_error(candidate_2):
        s= candidate_1
    else:
        s= candidate_2
        return s

print(classify(set_1[100]))


if plot:
    fig, ax = plt.subplots()
    ax.hist(set_1, color='red')
    ax.hist(set_2, color='blue')
    plt.show()
