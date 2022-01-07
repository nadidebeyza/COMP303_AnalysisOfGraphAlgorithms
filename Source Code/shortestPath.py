# Nadide Beyza Dokur
# Dijkstra's Shortest Path
# 06.01.2022

from datetime import datetime

# Get input from user
numberOfCities = int(input("Enter number of cities (N): "))
given_source = int(input("Enter a given source (S): "))
destination = int(input("Enter a destination (D): "))
# Initial declarations
source = given_source
cities = []
unvisitedCities = []
visitedCities = []
paths = []
numberOfPaths = 0
next_destination_weight = 0
probable_destinations = []  # It holds probable destinations of the current source
# Create unvisitedCities array and visitedCities array
for i in range(1, numberOfCities + 1):
    cities.append(i)
    unvisitedCities.append(i)
unvisitedCities.remove(given_source)
visitedCities.append(given_source)
# Create paths array: path[source node, target node, weight of the path btw source node and target node]
for i in range(given_source, destination + 1):
    for j in range(given_source, destination + 1):
        if abs(i - j) <= 3 and i != j:
            paths.append([i, j, i + j])
            numberOfPaths += 1
# Print initial situation
print("Paths between two cities: ")
print(paths)
start = datetime.now()
if source != destination:  # If there is no direct path from given source to destination
    for h in range(numberOfPaths):
        # Update probable destinations
        if paths[h][0] != paths[numberOfPaths - 1][0]:
            if paths[h][0] != paths[h - 1][0]:
                    if h != 0:
                        print("Unvisited cities:")
                        print(unvisitedCities)
                        print("Visited cities:")
                        print(visitedCities)
                    probable_destinations = []
        # Find paths with destination current source
        if paths[h][0] == source:
            for p in range(len(visitedCities)):
                if paths[h][1] != visitedCities[p]:
                    # Updating of visited cities and unvisited cities
                    if source not in visitedCities:
                        visitedCities.append(source)
                    if source in unvisitedCities:
                        unvisitedCities.remove(source)
                    # Creation of probable destinations array: probable_destinations[destination, weight]
                    if [paths[h][1], paths[h][2]] not in probable_destinations:
                        if paths[h][1] not in visitedCities:
                            probable_destinations.append([paths[h][1], paths[h][2]])
                    # Selection of next destination weight from probable_destinations
                    for g in range(len(probable_destinations)):
                        next_destination_weight = probable_destinations[0][1]
                        if next_destination_weight == 0 or next_destination_weight >= probable_destinations[g][1]:
                            next_destination_weight = probable_destinations[g][1]
                            # Update source
                            if paths[h][0] != paths[numberOfPaths - 1][0]:
                                if paths[h][0] != paths[h + 1][0]:
                                    source = probable_destinations[g][0]
    source = 0
    print("Unvisited cities:")
    print(unvisitedCities)
    print("Visited cities:")
    print(visitedCities)
    print("You arrived!")
else:  # If there is a direct path from given source to destination
    print("You arrived!")
print("Running time of the algorithm:")
print(datetime.now() - start)