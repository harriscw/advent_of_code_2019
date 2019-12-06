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


# wire1 = ['R8','U5','L2']
# wire2 = ['U7','R6','D2']

# wire1 = ['R8','U5','L5','D3']
# wire2 = ['U7','R6','D4','L4']

# wire2= ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire1= ['U62','R66','U55','R34','D71','R55','D58','R83']

# wire2= ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire1= ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

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
			finalxints.append(xints)
			finalyints.append(yints)
			
#get segment lengths per wire
w1steps = []
for i in range(len(w1segx)):
	w1steps.append(abs(w1segx[i][-1]-w1segx[i][0]) + abs(w1segy[i][-1]-w1segy[i][0]))
w2steps = []
for i in range(len(w2segx)):
	w2steps.append(abs(w2segx[i][-1]-w2segx[i][0]) + abs(w2segy[i][-1]-w2segy[i][0]))

# print(w1steps)
# print(w2steps)
# print(w1segx)
# print(w1segy)
# print(w2segx)
# print(w2segy)

# print(len(w1x))
# print(len(w1y))
# print(len(w2x))
# print(len(w2y))
# print(len(wire1))
# print(len(wire2))
# print(len(w1segx))
# print(len(w1segy))
# print(len(w1steps))
# print(len(w2segx))
# print(len(w2segy))
# print(len(w2steps))	
# print(len(finalxints))
# print(len(finalyints))

#iterate over intersections to find segments where there's an intersection

#get rid of [0,0]
finalxints=finalxints[1:]
finalyints=finalyints[1:]
# w1x=w1x[1:]
# w1y=w1y[1:]
# w2x=w2x[1:]
# w2y=w2y[1:]

#iterate over intersection points
stepstoint=[]
for i in range(len(finalxints)):
	print("The Int: ",finalxints[i],finalyints[i])
	# thisw1steps=0
	# thisw2steps=0
# for row in w1 find where w1(x) = int(x) and w1(y)=int(y)
#w1segx is all the integer points in the jth segment
	for j in range(len(w1segx)):
		if (finalxints[i][0] in w1segx[j] and finalyints[i][0] in w1segy[j]):
			# print(finalxints[j][0],finalyints[j][0])
			#get wire1 prior sum of steps and append to list
			print("Previous W1 steps",w1steps[0:j])
			#sums all previous steps
			w1sumprev=sum(w1steps[0:j])
			#now need to sum the partial steps
			w1partialseg = abs(finalxints[i][0]-w1x[j]) + abs(finalyints[i][0]-w1y[j])
			print("W1 partial: ",w1partialseg)
			#now sum these both
			thisw1steps=w1sumprev+w1partialseg
			print("W1 total", thisw1steps)
	for k in range(len(w2segx)):
		if (finalxints[i][0] in w2segx[k] and finalyints[i][0] in w2segy[k]):
			# print(finalxints[k][0],finalyints[k][0])
			#get wire1 prior sum of steps and append to list
			print("Previous W2 steps",w2steps[0:k])
			#sums all previous steps
			w2sumprev=sum(w2steps[0:k])
			#now need to sum the partial steps
			w2partialseg = abs(finalxints[i][0]-w2x[k]) + abs(finalyints[i][0]-w2y[k])
			print("w2 partial: ",w2partialseg)
			#now sum these both
			thisw2steps=w2sumprev+w2partialseg
			print("W2 total", thisw2steps)
			
	thisnewsum=thisw1steps+thisw2steps
	if thisnewsum !=0:
		stepstoint.append(thisnewsum)

print("Intersections")
print(finalxints)
print(finalyints)

print("Steps to ints")
print(stepstoint)

print("min")
print(min(stepstoint))


