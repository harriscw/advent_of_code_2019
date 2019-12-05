import csv

file=open("wire1.csv", "rt")
reader = csv.reader(file)
wire1 = []
for line in reader:
# 	print(line)
	for i in range(len(line)):
		wire1.append(line[i])

file=open("wire2.csv", "rt")
reader = csv.reader(file)
wire2 = []
for line in reader:
	# print(line)
	for i in range(len(line)):
		wire2.append(line[i])

# wire2= ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire1= ['U62','R66','U55','R34','D71','R55','D58','R83']



# mytest = ['R8','U5','L5','D3']

def coords(mytest):
	x = [0]
	y = [0]
	for value in mytest:
		
		if value[0]=="R":
			x.append(x[-1]+int(value[1:]))
			y.append(y[-1])
		if value[0]=="U":
			x.append(x[-1])
			y.append(y[-1]+int(value[1:]))
		if value[0]=="L":
			x.append(x[-1]-int(value[1:]))
			y.append(y[-1])
		if value[0]=="D":
			x.append(x[-1])
			y.append(y[-1]-int(value[1:]))
	return x,y
		
# print(coords(wire1))
# print(coords(wire2))

# libraries and data
import matplotlib.pyplot as plt
import pandas as pd
df1=pd.DataFrame({'x1values': coords(wire1)[0], 
                 'y1values': coords(wire1)[1]})
df2=pd.DataFrame({'x2values': coords(wire2)[0], 
                 'y2values': coords(wire2)[1] })

# plot
# axes = plt.gca()
# axes.set_xlim([600,700])
# axes.set_ylim([-10,0])
plt.plot( 'x1values', 'y1values', data=df1,color='red')
plt.plot( 'x2values', 'y2values', data=df2,color='blue')
plt.show()
# print(df)
