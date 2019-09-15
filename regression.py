from math import *

theta = [ 1, 1, 1 ]
x, y = [], []
alpha, previous_cost, factor = 0.000000000162, 0, 1 #已经很靠近最佳学习速率了

def read_data():
    # Model: x^2 - 10x + 5
    # Generated with `data-generater.py`
    data_x = open('./data/data_x.txt', 'rt')
    data_y = open('./data/data_y.txt', 'rt')

    xline, yline = data_x.readline(), data_y.readline()

    while xline != '':
        x.append(eval(xline))
        xline = data_x.readline()
    while yline != '':
        y.append(eval(yline))
        yline = data_y.readline()

def hypothesis(x):
    # theta_1 x^2 + theta_2 * x + theta_3
    return theta[0] * pow(x, 2) + theta[1] * x + theta[2]

def cost():
    r = 0
    for i in range(1, len(x)):
        r += pow(hypothesis(i) - y[i], 2)
    return r / len(x)

def adjast_parm():
    temp_theta = [0, 0, 0]
    for i in range(1,len(x)):
        temp_theta[0] += (hypothesis(i) - y[i]) * pow(i, 2)
        temp_theta[1] += (hypothesis(i) - y[i]) * i
        temp_theta[2] += hypothesis(i) - y[i]
    for i in range(0, 3):
        temp_theta[i] /= len(x)
        theta[i] -= temp_theta[i] * alpha

def train():
    global factor, alpha, previous_cost

    for i in range(1, 10000): # 不多bb，直接一万次
        for j in range(0, len(x)):
            adjast_parm()
            current_cost = cost()
            str = ''
            if previous_cost > current_cost:
                str = '\u25bc'
            else:
                str = '\u25b2'
            previous_cost = current_cost
            print('Cost = {},\tHypothesis = {}x^2 + {}x + {}'.format(current_cost, theta[0], theta[1], theta[2]) + '\t' + str)

read_data()
train()
