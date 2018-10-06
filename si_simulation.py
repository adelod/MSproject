import matplotlib.pyplot as plt
import numpy as np
import operator
file = open ("higgs-activity_time.txt", 'r')



infected = 0
infected_dict = {}
plot_x = [0]
plot_y = [0]
time = 0
node = 0
for i in file.readlines():
    source , dest, timestamp, type = [x for x in i.strip('\n').split(' ')]
    dest = int(dest)
    source = int(source)
    timestamp = int(timestamp)
    time += 0.1
    if type == 'RT':
        node += 1
        if source not in infected_dict:
            infected += 1
            infected_dict[source] = timestamp
        if source in infected_dict:
            if infected_dict[source] > timestamp:
                infected_dict[source] = timestamp
    if dest not in infected_dict:
        infected += 1
        infected_dict[dest] = timestamp
    if dest in infected_dict:
        if infected_dict[dest] > timestamp:
            infected_dict[dest] = timestamp

print "reading is done"

sorted_by = sorted(infected_dict.items(), key=operator.itemgetter(1))
print sorted_by[0:10]
final1 = []
final2 = []
for t in range(len(sorted_by)):
    final1.append(sorted_by[t][1])
    final2.append(t)
print node
plt.plot(final1, final2)
plt.show()

