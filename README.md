# A* Search Algorithm in Python
This Python script implements the A* search algorithm to find the shortest path between cities on a map. The map is represented as a dictionary of dictionaries, where each key is a city, and its value is another dictionary representing neighboring cities and the cost to reach them.

## Features
- Map Representation: The map is stored in a dictionary where keys are city names, and values are dictionaries of neighboring cities with travel costs.
- Heuristic Function: Uses the straight-line (Euclidean) distance between cities as a heuristic to estimate the cost to reach the goal.
- A Search Algorithm*: Finds the shortest path between the start city and the goal city using the A* search algorithm.

## Getting Started
## Prerequisites
- Python 3.x

## Running the Script
1- Clone the repository (if applicable):
```bash
git clone https://github.com/yourusername/astar-search.git
```

2- Run the script:
```bash
python astar_search.py
```

## Code Overview
- Map Definition
The map is defined as a dictionary where each city has a list of neighboring cities and the cost to reach them.

- Heuristic Function
The heuristic function estimates the distance between the current city and the goal city using the Euclidean distance.

- A* Search Function
The aStarSearch function performs the A* search algorithm to find the shortest path from the start city to the goal city.

- Running the Search
The script prompts the user to input the start and goal cities and then runs the A* search algorithm to find the shortest path.
