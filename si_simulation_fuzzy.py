from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
from numpy import corrcoef
import operator


fig = plt.figure()
# ax = Axes3D(fig)

file = open ("higgs-activity_time.txt", 'r')
lines = file.readlines()
infection = {0:456626 - 177247, 1:0, 2:0, 3:0}
node_infection = {}
node_infection_rate = {}
node_count = float(456626 - 177247 + 1000 )
t = 0
acts = len(lines)
per = 3
threshold = 12.0
z = [float(i) for i in range(1, per + 1) ]
defuzzy = []
no_fuzzy = []
T =[]
i = 0


def permutate(arr):

    arr.sort()
    temp = [0] * len(arr)
    turn = False
    c1 = 0
    c2 = 1
    for i in arr:
        if turn:
            temp[c1] = i
            turn = False
            c1+=1
        else:
            temp[-c2] = i
            turn = True
            c2+=1
    return temp


for line in lines:
    First = True
    t += 1
    source, dest, timestamp, type = [x for x in line.strip('\n').split(' ')]
    dest = int(dest)
    source = int(source)
    timestamp = int(timestamp)
    if source in node_infection_rate:
        if type == 'RT':
            node_infection_rate[source] += 1
        elif type == 'MT':
            node_infection_rate[source] += 2
        elif type == 'RE':
            node_infection_rate[source] += 3
    else:
        if type == 'RT':
            node_infection_rate[source] = 1
        elif type == 'MT':
            node_infection_rate[source] = 2
        elif type == 'RE':
            node_infection_rate[source] = 3

    if source in node_infection:

        if type not in node_infection[source]:
            node_infection[source].append(type)
            p = len(node_infection[source])
            infection[p] += 1
            infection[p - 1] -= 1
    else:
        a = node_infection_rate.values()
        m = max(a)
        b = [float(x)/m for x in a]
        s = sum(b)
        defuzzy.append(s)
        i += 1
        T.append(timestamp)
        no_fuzzy.append(i)
        node_infection[source] = [type]
        infection[1] += 1
        infection[0] -= 1
    if t == acts/per:
        # a = node_infection_rate.values()
        # m = max(a)
        # tt = 0
        # for i in range(len(a)):
        #     if a[i] > threshold:
        #         tt+=1
        #         a[i] = threshold
        #
        # a.extend([0]*infection[0])
        # a = permutate(a)
        # y1 = [float(o)/ threshold for o in a]
        #
        # k = len(y1)
        # x1 = [(100.0/ k) * i for i in range(k)]
        t = 0

        zeros = float(infection[0]) *  (1/node_count)
        ones = float(infection[1]) * (1 / node_count)
        twos = float(infection[2]) * (1 / node_count)
        threes = float(infection[3]) * (1 / node_count)
        x = np.array([
            .0,
             zeros / 4,
             zeros / 2 + ones / 4,
             zeros / 2 + ones / 2 + twos / 4,
             zeros / 2 + ones / 2 + twos / 2 + threes/2,
             zeros / 2 + ones / 2 + twos / 2 + threes + twos/4,
             zeros / 2 + ones / 2 + twos + threes + ones / 4,
             1 - zeros / 4,
            1.
        ])
        y = np.array([
           .0,
            .0,
            1 / float(3),
            2 / float(3),
            1.,
            2 / float(3),
            1 / float(3),
            .0,
            .0
        ])
        # plt.plot(x,y)



# plt.show()
plt.plot(T, defuzzy)
plt.plot(T, no_fuzzy)
plt.show()
