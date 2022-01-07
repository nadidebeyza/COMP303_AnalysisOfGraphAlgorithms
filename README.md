### Analysis of Graph Algorithms

**Part 1: Shortest Path**

This section of the project includes a Python3 program that uses Dijkstra's shortest route method to identify the shortest path between provided source (S) and destination (D) nodes in a graph. The nodes in the graph represent cities, and the weights on the edges represent the time it takes to travel between them. The graph consists of 2 x N/2 nodes as shown below.

[![For N = 6, 2 x N/2 Nodes](https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/92851aae36350525479ce0dc3258a63ed22eedb1/2xN:2_nodes_diagram.png "For N = 6, 2 x N/2 Nodes")](http://https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/92851aae36350525479ce0dc3258a63ed22eedb1/2xN:2_nodes_diagram.png "For N = 6, 2 x N/2 Nodes")

If | I - j | = 3, and I and j are not equal, there is an edge from node I to node j, as seen in this graph. The program is given the number of cities, N, as well as the source (S) and destination (D) cities.

[shortestPath.py](https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/1990796481474125c560920f9eafb08442280f1c/Source%20Code/shortestPath.pyhttp:// "shortestPath.py")

> This section of Part 1 discusses Dijkstra's shortest route algorithm. The algorithm's running time was calculated by adding the running times of each line in the algorithm. When the distance between two cities, wij = i + j if |i-j| = 3, and I and j are not the same, the output indicates the stages of the method for N=10, S=1, D=6. The rest of the weights are infinite.

[![Example output of the code](https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/1990796481474125c560920f9eafb08442280f1c/Output/shortestPath_output1.png "Example output of the code")](https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/1990796481474125c560920f9eafb08442280f1c/Output/shortestPath_output1.png "Example output of the code")

[![Another example output of the code](https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/87b1f699f53e6b5cbb138b9cad0af6f5d91f0c57/Output/shortestPath_output2.png "Another example output of the code")](http://https://github.com/nadidebeyza/COMP303_AnalysisOfGraphAlgorithms/blob/87b1f699f53e6b5cbb138b9cad0af6f5d91f0c57/Output/shortestPath_output2.png "Another example output of the code")