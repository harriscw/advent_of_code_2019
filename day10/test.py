
# print(range(5))
for row in range(5):
	print(row)

import csv

file=open("test1.csv", "rt")
reader = csv.reader(file)
mydata = []
for line in reader:
	# print(line)
	for i in range(len(line)):
		mydata.append(line[i])
		
print(''.join(mydata))



			#if horizontal component equal
			elif otherpt[0] == givenpt[0]:
				if otherpt[1] > givenpt[1]:
					myslope='+V'
				else:
					myslope='-V'
			#if vertical component equal
			elif otherpt[1] == givenpt[1]:
				if otherpt[0] > givenpt[0]:
					myslope='+H'
				else:
					myslope='-H'
			#Distinguishing quadrants