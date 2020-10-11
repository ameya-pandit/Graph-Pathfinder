import networkx as nx
import csv

listOfPaths = []

#retrives all the paths in the graph in between the two nodes that are inputted by the user.
def is_path(g, nodeA, nodeB):
    nodeA = str(nodeA)
    nodeB = str(nodeB)
        
    #if nodes exist
    if g.has_node(nodeA) and g.has_node(nodeB):
        #if path exists between node A and B
        if (nx.has_path(g, nodeA, nodeB)):
            #retrieve ALL the paths between node A and B
            paths = nx.all_simple_paths(g, source=nodeA, target=nodeB)
            
            #get all the edges from the paths that exist between node A and B
            for path in map(nx.utils.pairwise, paths):
                edges = list(path)
                listOfPaths.append(edges)
    
totalWeight = 0
rightWeightPaths = []

#retrieve the total weight for all the edges from all the paths. Then, compare the total weight with the weight limit set by the user input
def total_weight(g, weightLimit):
    for path in listOfPaths:
        weightOfPaths = 0
       
        for p in path:
            #retrieve the weight value from the edges
            for tuple in g.edges.data('weight'):
                if p[0] in tuple:
                    if p[1] in tuple:
                        weightOfPaths += float(tuple[2])
            #get the total weight which is a sum of the weight of all the edges
            totalWeight = weightOfPaths
        
        if round(totalWeight, 4) < float(weightLimit):
            rightWeightPaths.append(path)

pathThatWorks = []
#similar to the total_weight function, this color function retrieves the color data of all the edges and compares with the total number of edges with the specific color chosen by user input allowed per the user input
def color(g, numberPaths, colorChoice):
    for path in rightWeightPaths:
        listOfColors = []
        for p in path:
            #retrieve the color value from all the edges
            for tuple in g.edges.data('color'):
                if p[0] in tuple:
                    if p[1] in tuple:
                        listOfColors.append(tuple[2])
                        
        if colorChoice in listOfColors:
            count = listOfColors.count(colorChoice)
            #if color count is less than the user input limit
            if count < numberPaths:
                pathThatWorks.append(path)

#prints out the output after getting the appropriate path
def output():
    #path counter used for output
    pathCounter = 0
    
    with open('output.csv', mode='w') as outputFile:
        #if there is a path that exists that fits all the criteria
        if (len(pathThatWorks) > 0):
            for path in pathThatWorks:
                #increment path counter
                pathCounter += 1
                outputFile.write('path_%s\n' % (pathCounter))
                
                #properly output the datta from the path per the specification
                for p in path:
                    outputFile.write("%s, %s\n" % (p[0], p[1]))
        #if no path exists, output a NULL
        else:
            outputFile.write('path_1\n')
            outputFile.write("NULL\n")
        
            

