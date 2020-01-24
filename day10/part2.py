#get all the signed slopes relative to my final coordinate that can see the most asteroids
#order them by quadrant and then slope
#go: UR->LR->LL->UL
#iterate over ordered list, add coordinate to final list when its hit then remove it from iterated list?
#maybe while asteroid list isn't empty?

import csv
#############
#read in data
#############

#test cases

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

########
#Reshape
########
import pandas as pd
import textwrap

#get segments
mylist = textwrap.wrap(myinput, myncol)
#convert to df
df=pd.DataFrame(mylist,columns=['orig'])

#######################
#get coordinates of asteroids
#######################

coords=[]
for col in range(myncol):
	for row in range(mynrow):
		if df.loc[row]['orig'][col]=='#':
			coords.append([col,row])
print(coords)

##############
#iterate over each asteroid
##############

#get a list of the slope between given asteroid and all other asteroids
#then assign a direction to each since asteroids with same slope can be in opposite directions from the given asteroid
#finally find the unique direction-ified slope values in that list per asteroid


for givenpt in [[26,29]]:
	slopenums=[]
	thecoord=[]
	for otherpt in coords:
		#dont get slope if points are equal
		if givenpt != otherpt:
			#calculate slope
			#if horizontal component not equal (avoid divide by 0)
			if otherpt[0] != givenpt[0]:
				myslope=str(-((otherpt[1]-givenpt[1])/(otherpt[0]-givenpt[0])))
			else:
				myslope='Inf'
			#apply quadrants
			if otherpt[0] >= givenpt[0] and otherpt[1] >= givenpt[1]:
				myslope="2. LR"+myslope
			elif otherpt[0] >= givenpt[0] and otherpt[1] < givenpt[1]:
				myslope="1. UR"+myslope
			elif otherpt[0] < givenpt[0] and otherpt[1] >= givenpt[1]:
				myslope="3. LL"+myslope
			elif otherpt[0] < givenpt[0] and otherpt[1] < givenpt[1]:
				myslope="4. UL"+myslope
			#debug
			# print("slope between: ",givenpt," and ",otherpt," : ",str(myslope))
			slopenums.append(myslope)
			thecoord.append(otherpt)

# print(len(slopenums))
# print(len(thecoord))

#mark space station asteroid with an X
df.loc[29,'orig']='.#......#...#...#.##......X..#.........'
# print(df)

#Convert lists into a dataframe
import pandas as pd
slopedf = pd.DataFrame({'slope':slopenums,'coords':thecoord})

#find distance
#sqrt((x2-x1)^2 + (y2-y1)^2)
import math
thedistance=[]
for coord in coords:
	if coord != [26,29]:
		thedistance.append(math.sqrt(((coord[0]-26)**2)+((coord[1]-29)**2)))

#sort dataframe by quadrant and slope and distance
slopedf['distance'] = thedistance

#create quadrant variable
slopedf['quadrant']=slopedf['slope'].str[:5]

#create numeric slope var
slopedf['slope2']=slopedf['slope'].str[5:].astype(float)


# drop original slope
slopedf=slopedf.drop(['slope'],axis=1)

#####
#sort
#####
#sort by quadrant, angle, distance
slopedf.sort_values(by=['quadrant','slope2','distance'],ascending=[True,False,True],inplace=True)

#this value should be -inf, not inf
slopedf.loc[250,'slope2']=-slopedf.loc[250,'slope2']

slopedf.sort_values(by=['quadrant','slope2','distance'],ascending=[True,False,True],inplace=True)
with pd.option_context('display.max_rows',None):
	print(slopedf)


#####
# iterate
#####
# do a while counter <200, 
# iterate over rows in df, if  i !=i+1 append to list and delete from df.  
mycnt=0
keepgoing=True
blasted=[[26,26]]
dropindex=[]
while keepgoing==True:
	slopedf.drop(dropindex)
	dropindex=[]
	for row in range(len(slopedf)):
		if slopedf.iloc[row]['slope2'] == slopedf.iloc[row+1]['slope2']:
			continue
		else:
			mycnt+=1
			blasted.append(slopedf.iloc[row+1]['coords'])
			dropindex.append(row+1)
		if mycnt==200:
			keepgoing=False
			break
print(df)			
print(blasted)
print(len(blasted))





