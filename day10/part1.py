import csv

#read in data
# filename="test0.csv"
# mynrow=5
# myncol=5

# filename="test1.csv"
# filename="test2.csv"
# filename="test3.csv"
# mynrow=10
# myncol=10

# filename="test4.csv"
# mynrow=20
# myncol=20

filename="finaltest.csv"
mynrow=39
myncol=39


file=open(filename, "rt")
reader = csv.reader(file)
mydata = []
for line in reader:
	# print(line)
	for i in range(len(line)):
		mydata.append(line[i])
		
myinput=''.join(mydata)

# print(myinput)

#get dimensions
import pandas as pd
import textwrap

#get segments
mylist = textwrap.wrap(myinput, myncol)
#convert to df
df=pd.DataFrame(mylist,columns=['orig'])
# print(df)
# print(df.loc[0]['orig'][0:2])

#get coordinates of asteroids
coords=[]
for col in range(myncol):
	for row in range(mynrow):
		if df.loc[row]['orig'][col]=='#':
			coords.append([col,row])
print(coords)

#iterate over each asteroids
#get a list of the slope between given asteroid and all other asteroids
#find the unique values in that list per asteroid

coi=[5,8]
finallist=[]
mydebug=[]
for givenpt in coords:
	slopenums=[]
	for otherpt in coords:
		#dont get slope if points are equal
		if givenpt != otherpt:
			#calculate slope
			#if horizontal component not equal
			if otherpt[0] != givenpt[0]:
				myslope=str((otherpt[1]-givenpt[1])/(otherpt[0]-givenpt[0]))
			else:
				myslope='V'
			#apply quadrants
			# if givenpt==coi:
				# print(" givenpt[0]: "+ str(givenpt[0]) + ", otherpt[0]: "+str(otherpt[0]))
			if otherpt[0] >= givenpt[0] and otherpt[1] >= givenpt[1]:
				myslope="LR"+myslope
			elif otherpt[0] >= givenpt[0] and otherpt[1] < givenpt[1]:
				myslope="UR"+myslope
			elif otherpt[0] < givenpt[0] and otherpt[1] >= givenpt[1]:
				myslope="LL"+myslope
			elif otherpt[0] < givenpt[0] and otherpt[1] < givenpt[1]:
				myslope="UL"+myslope
				

			#debug
			# if givenpt==coi:
				# print("slope between: ",givenpt," and ",otherpt," : ",str(myslope))
				# mydebug.append(myslope)
			slopenums.append(myslope)
	finallist.append(len(set(slopenums)))
	
print(df)
print("Coordinates")
print(coords)	
print("Lengths")
print(finallist)
thepos=finallist.index(max(finallist))
print("the max: ",max(finallist),"coordinate: ",coords[thepos])
# print("Debug")
# print(set(mydebug))
# print(len(set(mydebug)))