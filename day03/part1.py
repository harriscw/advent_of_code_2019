from __future__ import division
import csv

file=open("wire1.CSV", "rt")
reader = csv.reader(file)
wire1 = []
for line in reader:
	# print(line)
	for i in range(len(line)):
		wire1.append(line[i])

file=open("wire2.CSV", "rt")
reader = csv.reader(file)
wire2 = []
for line in reader:
	# print(line)
	for i in range(len(line)):
		wire2.append(line[i])

# wire2= ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire1= ['U62','R66','U55','R34','D71','R55','D58','R83']

# wire2= ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire1= ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

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
# print(mytest)		
# print(coords(mytest))

# print(coords(wire1)[0])
# print("\n")
# print(coords(wire1)[1])
# print("\n")
# print("\n")	
# print(coords(wire2)[0])
# print("\n")
# print(coords(wire2)[1])

# L1 = line([0,0],[997,0])	
# L2 = line([0,0],[-997,0])	

#these get x and y coordinates of each segment of each wire
w1x = coords(wire1)[0]
w1y = coords(wire1)[1]
w2x = coords(wire2)[0]
w2y = coords(wire2)[1]

# print(w1x)
# print(w1y)
#now lets get the unique x and y values per segment per wire

w1segx = []
w1segy = []
for i in range(len(w1x)-1):
	newval=list(range(min(w1x[i],w1x[i+1]),max(w1x[i],w1x[i+1])+1))
	w1segx.append(newval)
	newval=list(range(min(w1y[i],w1y[i+1]),max(w1y[i],w1y[i+1])+1))
	w1segy.append(newval)
	
# print(w1segx)
# print(w1segy)

w2segx = []
w2segy = []
for i in range(len(w2x)-1):
	newval=list(range(min(w2x[i],w2x[i+1]),max(w2x[i],w2x[i+1])+1))
	w2segx.append(newval)
	newval=list(range(min(w2y[i],w2y[i+1]),max(w2y[i],w2y[i+1])+1))
	w2segy.append(newval)	

#now lets find points in common between segments
finalxints = []
finalyints = []
for i in range(len(w1segx)):
	for j in range(len(w2segx)):
		xints = list(set(w1segx[i]).intersection(w2segx[j]))
		yints = list(set(w1segy[i]).intersection(w2segy[j]))
		if len(xints)>0 and len(yints)>0:
			# print("intersection found")
			# print("Element on w1/w2 list",i,"/", j)
			# print("Common X values:",xints)
			# print("Common Y values:",yints)
			finalxints.append(xints)
			finalyints.append(yints)
#now populate the manhattan distance for each intersection point and find the minimum
mandists = []
for i in range(len(finalxints)):
	thedist = abs(finalxints[i][0]) + abs(finalyints[i][0])
	# print(thedist)
	if thedist != 0:
		mandists.append(thedist)
print(min(mandists))