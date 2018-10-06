import networkx as nx
import numpy as np
from numpy import corrcoef
import operator


file = open ("higgs-activity_time.txt", 'r')
lines = file.readlines()
node_infection = {}
node_info = {}
node_count = float(456626 - 177247 + 1000 )
G = nx.DiGraph()



for line in lines:

    source, dest, timestamp, type = [x for x in line.strip('\n').split(' ')]
    dest = int(dest)
    source = int(source)
    timestamp = int(timestamp)
    if source in node_info:
        if type == 'RT':
            node_info[source][0] += 1
        elif type == 'MT':
            node_info[source][0] += 2
        elif type == 'RE':
            node_info[source][0] += 3
    else:
        if type == 'RT':
            node_info[source] = [1, 0, 0]
        elif type == 'MT':
            node_info[source] = [2, 0, 0]
        elif type == 'RE':
            node_info[source] = [3, 0, 0]
file.close()

file = open("higgs-social_network.edgelist.txt",'r')
edges = file.readlines()
print len(edges)

for edge in edges:
    source, dest = [x for x in edge.strip('\n').split(' ')]
    dest = int(dest)
    source = int(source)
    if source in node_info:
        node_info[source][1] +=1
    # else:
    #     node_info[source] = [0,1,0]
    if dest in node_info:
        node_info[dest][2] += 1
    # else:
    #     node_info[dest] = [0,0,1]
print ("nodes with most in degrees:")
print (sorted(node_info.items(), key= lambda x:x[1][2], reverse=True)[:10])
print ("nodes with most out degrees:")
print (sorted(node_info.items(), key= lambda x:x[1][1], reverse=True)[:10])
print ("most infected nodes:")
print (sorted(node_info.items(), key= lambda x:x[1][0], reverse=True)[:10])
din = []
dout = []
infection = []
print "done 1"
for x in node_info:
    din.append(node_info[x][2])
    dout.append(node_info[x][1])
    infection.append(node_info[x][0])
print "done 2"
print corrcoef(din , infection)
print corrcoef(dout, infection)
print corrcoef(din, dout)

    #
    # if source in node_infection:
    #
    #     if type not in node_infection[source]:
    #         node_infection[source].append(type)
    #         p = len(node_infection[source])
    #         infection[p] += 1
    #         infection[p - 1] -= 1
    # else:
    #
    #     defuzzy.append(float(infection[1] + 2 * infection[2] + 3 * infection[3]) / 3)
    #     i += 1
    #     T.append(timestamp)
    #     no_fuzzy.append(i)
    #     node_infection[source] = [type]
    #     infection[1] += 1
    #     infection[0] -= 1
