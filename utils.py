import matplotlib.pyplot as plt
x1, y1 = [5 ,12, 3], [1, 4,2]
x2, y2 = [0,1 ], [0,1]
plt.plot(x1, y1,x2,y2, marker = 'o')


plt.autoscale([0,0])

plt.show()