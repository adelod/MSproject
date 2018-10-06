import networkx as nx
import numpy.random as rand
from sets import Set


file = open ("higgs-social_network.edgelist.txt", 'r')
lines = file.readlines()
print(len(lines))
i = 0
adj = {}
infected_nodes = {}
beta = .3
vul = {}
infection = 0.
infection_prime = 0.
node = []
for line in lines[:100000]:

    source, dest = [x for x in line.strip('\n').split(' ')]
    dest = int(dest)
    source = int(source)
    if source in adj:
        adj[source].append(dest)
    else:
        adj[source] = [dest]
        if rand.random_integers(100) ==99:
            infected_nodes[source] = 1.
            infection_prime += 1.
    for i in infected_nodes.keys():
        if i in adj:
            for x in adj[i]:
                if rand.rand() <= beta:
                    if x not in infected_nodes:
                        infected_nodes[x] = 0.
                    temp = infected_nodes[x]
                    infected_nodes[x] = min(1., infected_nodes[x] + vul[x] * infected_nodes[i])
                    infection += infected_nodes[x] - temp
    print infection - infection_prime
    infection_prime = infection
    print len(infected_nodes)
