import sys
import csv
import networkx as nx

#only use this for testing if the graph is set up
import matplotlib.pyplot as plt

#importing the function file
import function

#this is the problem assigned to us:
#find s where is_path(s, A, B) and total_weight(s, t) and color(s, Color, u) and t<C and u<D

g = nx.Graph()

#setting up the graph
def setUpGraph(firstNode, secondNode, edgeWeight, edgeColor):
    g.add_edge(firstNode, secondNode, weight=edgeWeight, color=edgeColor)

#if no csv file inputted, exit the program
if (len(sys.argv) < 2):
    print("Enter the CSV file as an input! Missing an input.")
    exit(0)
    
#csv file is set to the next input after file name
csvFile = sys.argv[1]

#opening and parsing the CSV file to set up the graph
with open(csvFile) as inputFile:
    csvRead = csv.reader(inputFile, delimiter=',')
    counter = 0
    
    for row in csvRead:
        nodeOne = row[0]
        nodeTwo = row[1]
        weight = row[2]
        color = row[3]
        
        #calling the graph set up function with the inputs from the csv file
        setUpGraph(nodeOne, nodeTwo, weight, color)

#while loop to make sure proper inputs are inputted
while True:
    try:
        inputA = int(input("Enter A: "))
        inputB = int(input("Enter B: "))
        inputC = float(input("Enter C: "))
        inputD = int(input("Enter D: "))
        inputColor = str(input("Enter Color: "))
        
        #if a number entered for the color question, exit the program. Improper input.
        if not (inputColor.isalpha()):
            print("Color should be a string value filled with letters!")
            exit(0)
            
    except ValueError:
        print("Sorry, re-enter the values properly.")
        print("Enter an integer value for A, B, and D. Enter a float value for C. Enter a string value for inputColor.")
        continue
    else:
        break
    
#just used this to make sure the graph was set up
#nx.draw(g, with_labels=True)
#plt.draw()
#plt.show()

#calling all the functions from the imported function file
function.is_path(g, inputA, inputB)
function.total_weight(g, inputC)
function.color(g, inputD, inputColor)
function.output()
