import re

# print('2'>'1')

# print([True,True,False].count(True))

# i = 2
# pattern1 = re.compile(r"[^2]22[^2]")
# pattern = re.compile(r"2{2}")
# pattern1 = re.compile(r"[^2]22[^2]")
# pattern2 = re.compile(r"[^2]22[^2]")

finallist = ['112233','113333','133344','123444','111122','255599']

goodones=[]
for thenum in finallist:
	thisnumber=[]
	for i in range(9):

		#1. Middle: for doubles in middle e.g. (*)(!4)(4)(4)(!4)(*)
		pattern1 = "[^" + str(i)+"]"+str(i)+str(i)+"[^" +str(i)+"]"
		#2a. Start: for doubles at start e.g. (4)(4)(!4)(*)(*)(*)
		pattern2 = "^" + str(i)+str(i)+"[^" +str(i)+"]"
		#2b. make sure the last 3 aren't a group of 4
		# actually don't need this because numbers cant decrease
		# pattern2b = re.compile(r"[^" + str(i)+str(i)+str(i)+"]$")
		#3a. End:
		pattern3 = "[^" + str(i)+"]"+str(i)+str(i)+"$"
		
		# print(re.search(pattern1 or pattern2 or pattern3,'1223344'))
		thisnumber.append(re.search("|".join([pattern1,pattern2,pattern3]),thenum) is not None)

	# print(thisnumber)
	if thisnumber.count(True)>0:
		# print("yessir")
		goodones.append(thenum)

print(finallist)
print(goodones)		
		