import matplotlib.pyplot as plt
import random

plt.ion() # turning interactive mode on

# preparing the data
y = [random.randint(1,10) for i in range(20)]
# x = [*range(1,21)]
# print(x)

a = 3

# plotting the first frame
graph = plt.plot(y)[0]
plt.plot(a,0,'ro')
plt.ylim(0,10)
plt.pause(1)

# the update loop
while(True):
	# updating the data
	# y.append(random.randint(1,10))
	# x.append(x[-1]+1)
	
    y = [x*0.8 for x in y]
	
	# removing the older graph
    graph.remove()
	
	# plotting newer graph
    graph = plt.plot(y,color = 'g')[0]
	# plt.xlim(x[0], x[-1])
	
	# calling pause function for 0.25 seconds
    plt.pause(0.25)
