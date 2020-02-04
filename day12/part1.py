import pandas as pd

#####################
# Read in data
#####################

#read in data and convert to list
myinput = open("final.txt",'r').read()
dfsplit = myinput.split('\n')
print(dfsplit)

#Clean up and create a data frame of coordinates
newlist = []
myx = []
myy = []
myz = []
for i in dfsplit:
	temp = i.replace("<","").replace(">","").replace("x=","").replace("y=","").replace("z=","").replace(" ","").split(",")
	myx.append(temp[0])
	myy.append(temp[1])
	myz.append(temp[2])

df = pd.DataFrame({
'x':pd.to_numeric(myx,errors='coerce'),
'y':pd.to_numeric(myy,errors='coerce'),
'z':pd.to_numeric(myz,errors='coerce')
})

# print(df)

#####################
# Calculate position, cumulative velocity, and total energy
#####################

#These for loops iterate over each column of the coordinate data frame 
# to compare each cell in a given column to each other cell

# initialize some empty objects
cumvel = df.replace(df, 0)
steps = 0

#number of steps is defined by the problem

while steps <=1000:
	finallist=[]

	#iterate over columns
	for column in df:
		thisvel = []
		#iterate over each value within columns
		for i in range(len(df[column])):
			mycnt=0 #counter for +1/-1 for each value
			#iterate over each other value in that column
			for othercell in df[column]:
				# print("cell: "+str(df[column][i])+" other cell: " +str(othercell))
				if othercell>df[column][i]:
					mycnt+=1
				elif othercell<df[column][i]:
					mycnt +=-1
			thisvel.append(mycnt)
		finallist.append(thisvel)
	
	# print(finallist)
	#Now create a velocity dataframe for current given coordinates
	vel = pd.DataFrame(finallist)
	vel = vel.transpose()
	vel.columns = ["x","y","z"]

	# print("Position")
	# print(df)
	# print("Velocity")
	# print(cumvel)
	
	# to get total energy in the system:
	# multiply the sum of the absolute values across x,y,z position and sum of the absolute values across x,y,z velocity, then sum it all up
	print("Step: ",str(steps)," , Total Energy: ",(df.abs().sum(axis=1)*cumvel.abs().sum(axis=1)).sum(axis=0))
	
	#update cumulative velocity, position, and steps
	cumvel = cumvel+vel
	df = df+cumvel
	steps+=1
