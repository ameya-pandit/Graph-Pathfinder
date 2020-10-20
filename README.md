# Graph-Pathfinder

# Summary #
This Python program reads in "path" (individual edges) values from a CSV (node A, node B, weight of edge, color of edge) and builds a graph with all of these edges. The user can then input two nodes from the graph, the max path weight value, the color, and the number of edges allowed of that color in the path between the nodes. 

# Technologies Used #
I utilized the networkx Python library to put together the graph after I retrieved the values from the CSV file (by parsing it). I tested whether or not the graph was build properly by using the matprotlib Python library to draw out the graph visually. 

# Files #
main.py reads the input CSV file, and builds the graph. 

function.py finds the path (if there is one) between two nodes on the graph, calculates the total weight of all the edges in the path (and compares with the max value the user inputted), checks whether there are a certain number of paths max of a certain color (number of paths and the color both inputted by the user), and outputs the edges in the path if one exists that satisfies the aforementioned conditions.
