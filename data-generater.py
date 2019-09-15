from random import random
import math

def func(x):
    return math.pow(x, 2) - x * 10 + 5

def randomize(x):
    if random() > 0.5:
        return func(x) + random() * 5
    return func(x) - random() * 5

def generate():
    file_x = open('./data/data_x.txt', 'wt')
    file_y = open('./data/data_y.txt', 'wt')
    for i in range(1, 500):
        file_x.writelines('{}\n'.format(i))
        file_y.writelines('{}\n'.format(randomize(i)))

generate()