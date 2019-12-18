import networkx as nx
import csv

# file=open("input.csv", "rt")
# reader = csv.reader(file)
# raworbits3 = []
# for line in reader:
	# for i in range(len(line)):
		# raworbits3.append(line[i])


raworbits1 = [
"A)B",
"B)C",
"B)D",
"D)E"]

raworbits2 = [
"COM)B",
"B)C",
"C)D",
"D)E",
"E)F",
"B)G",
"G)H",
"D)I",
"E)J",
"J)K",
"K)L"
]

orbits = [x.split(')') for x in raworbits1]

#create graph
G=nx.DiGraph()

#get unique nodes & add to graph
print(orbits)
mynodes=[]
for i in orbits:
	mynodes.append(i[0])
	mynodes.append(i[1])


mynodes=list(set(mynodes))
G.add_nodes_from(mynodes)

#add edges
tupelized = []
for i in orbits:
	tupelized.append((i[0],i[1]))

G.add_edges_from(tupelized)

for path in nx.all_simple_paths(G, source="C", target="A"):
	print(path)

