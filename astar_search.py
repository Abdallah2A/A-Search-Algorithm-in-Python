import heapq

# Define the map as a dictionary of dictionaries
# to know every neighbors for every city and the cost to go to it
map = {
    'Alexandria': {'Beheira': 80.1, 'Matruh': 329.6},
    'Aswan': {'Luxor': 238, 'Red Sea': 505.6, 'New Valley': 582},
    'Asyut': {'Sohag': 97.3, 'Minya': 174.1,'Red Sea': 417.4, 'New Valley': 497},
    'Beheira': {'Alexandria': 85.7, 'Kafr El Sheikh': 93.9, 'Gharbia': 105.6, 'Giza': 178.8, 'Matruh': 379.7, 'Monufia': 107.7},
    'Beni Suef': {'Minya': 143, 'Giza': 325.3, 'Faiyum': 46.1, 'Red Sea': 418.5, 'Suez': 247.2},
    'Cairo': {'Giza': 5.1, 'Suez': 139.4, 'Qalyubia': 37.1, 'Ismailia': 127.5, 'Sharqia':110.8},
    'Dakahlia': {'Damietta': 48.5, 'Sharqia': 72.1, 'Kafr El Sheikh': 77.3, 'Gharbia': 68.7, 'Port Said': 101},
    'Damietta': {'Dakahlia': 50.8, 'Port Said': 56},
    'Faiyum': {'Beni Suef': 44.8, 'Giza': 96.2},
    'Gharbia': {'Beheira': 99.4, 'Kafr El Sheikh': 31.3, 'Monufia': 47.7, 'Dakahlia': 70.6, 'Sharqia': 107, 'Qalyubia': 83.1},
    'Giza': {'Cairo': 6, 'New Valley': 726, 'Matruh': 483.6,'Beheira': 170.8, 'Beni Suef': 141.96, 'Qalyubia': 41.9, 'Monufia': 86.1, 'Suez': 151.1, 'Faiyum': 94.9},
    'Ismailia': {'Suez': 227.3, 'Port Said': 81.3, 'Sharqia': 77.8, 'North Sinai': 163.2},
    'Kafr El Sheikh': {'Beheira': 94, 'Dakahlia': 77.1, 'Gharbia': 34},
    'Luxor': {'Qena': 81.4, 'Aswan': 241.3, 'New Valley': 564, 'Red Sea': 220.9},
    'Matruh': {'Alexandria': 351.1, 'Giza': 286.2, 'New Valley': 757, 'Beheira': 407.6},
    'Minya': {'Beni Suef': 146.2, 'Asyut': 144.7, 'New Valley': 532, 'Red Sea': 413.3},
    'Monufia': {'Gharbia': 43, 'Giza': 96.8, 'Beheira': 101.2, 'Qalyubia': 51.9, 'Sharqia': 95.6, 'Dakahlia': 120.4},
    'New Valley': {'Aswan': 582, 'Luxor': 564, 'Qena': 585, 'Sohag': 506, 'Asyut': 497, 'Minya': 532, 'Giza': 726, 'Matruh': 757},
    'North Sinai': {'South Sinai': 120, 'Suez': 146.3},
    'Port Said': {'Ismailia': 82.6, 'Sharqia': 107.6, 'North Sinai': 233.7, 'Dakahlia': 98.7, 'Damietta': 52.8},
    'Qalyubia': {'Cairo': 41.6, 'Sharqia': 82.6, 'Giza': 51.9, 'Gharbia': 70.7, 'Monufia': 49.5, 'Dakahlia': 110.6},
    'Qena': {'Luxor': 68.4, 'Sohag': 56.7, 'New Valley': 585, 'Red Sea': 171.2},
    'Red Sea': {'Luxor': 227, 'Sohag': 357.6, 'Aswan': 716, 'Qena': 178.3, 'Minya': 415.1, 'Asyut': 417.7 ,'Beni Suef': 420.7, 'Suez': 382.5},
    'Sharqia': {'Dakahlia': 72, 'Qalyubia': 86.2, 'Gharbia': 116.3, 'Monufia': 95.1, 'Cairo': 112.2, 'Port Said': 113.5, 'Ismailia': 76.6},
    'Sohag': {'Asyut': 159.2, 'Red Sea': 355, 'Qena': 50.6, 'New Valley': 506},
    'South Sinai': {'North Sinai': 120, 'Suez': 171},
    'Suez': {'Ismailia': 90.7, 'North Sinai': 174.4, 'South Sinai': 171, 'Sharqia': 140, 'Cairo': 140.2, 'Giza': 150.2, 'Red Sea': 413.1}
}

def heuristic(currentCity, goalCity):
    """    
    Estimate the distance between currentCity and goalCity using straight-line distance.
    Calculate h(n) for every city.

    Args:
        currentCity (string): The City you already on it
        goalCity (string): The City you need to reach it

    Returns:
        double: The distance between the current City and the goal City by coordinate system
    """
    
    # Define the coordinates of each city as a dictionary
    coordinates = {
        'Alexandria': (31.2156, 29.9553),
        'Aswan': (24.0889, 32.8998),
        'Asyut': (27.1809, 31.1837),
        'Beheira': (30.9569, 30.4180),
        'Beni Suef': (29.0661, 31.0999),
        'Cairo': (30.0444, 31.2357),
        'Dakahlia': (31.0806, 31.4117),
        'Damietta': (31.4165, 31.8133),
        'Faiyum': (29.3084, 30.8428),
        'Gharbia': (30.7942, 30.9990),
        'Giza': (30.0131, 31.2089),
        'Ismailia': (30.6043, 32.2722),
        'Kafr El Sheikh': (31.1090, 30.9360),
        'Luxor': (25.6872, 32.6396),
        'Matruh': (31.3547, 27.2373),
        'Minya': (28.1099, 30.7503),
        'Monufia': (30.5877, 31.5069),
        'New Valley': (25.3714, 29.2154),
        'North Sinai': (31.1356, 33.8357),
        'Port Said': (31.2653, 32.3019),
        'Qalyubia': (30.3265, 31.2357),
        'Qena': (26.1644, 32.7263),
        'Red Sea': (26.3549, 33.7647),
        'Sharqia': (30.5467, 31.5326),
        'Sohag': (26.5569, 31.6948),
        'South Sinai': (28.4173, 34.0467),
        'Suez': (29.9669, 32.5498)
    }
    
    # Extract the coordinates of the current city and the goal city from the dictionary
    x1, y1 = coordinates[currentCity]
    x2, y2 = coordinates[goalCity]
    
    # Calculate the Euclidean distance between the two cities using the distance formula
    euclideanDistance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return euclideanDistance

def aStarSearch(map, startCity, goalCity):
    """
    This function performs an A* search on a dictionary of cities
    represented by map, starting at startCity and ending at goalCity.
    A* search retunes shortest paths from start city to goal city.

    Args:
        map (Dictionary): Dictionary have cities and it neighbors 
        startCity (String): The City you need to start search from it
        goalCity (String): The City you need to reach it

    Returns:
        List: The shortest path from start city to goal city
    """
    # Checks if start city and goal city in map or not
    if startCity not in map and goalCity not in map:
        print("Both start city and goal city are not in map")
        return None
    elif startCity not in map:
        print("Start city is not found in the map.")
        return None
    elif goalCity not in map:
        print("End city is not found in the map.")
        return None
    
    priorityQueue = [(0, startCity)]
    visitedList  = set()
    # Cost so far to reach goal
    gCost = {startCity: 0}
    # Estimated total cost of path through start city to reach goal city
    fCost = {startCity: heuristic(startCity, goalCity)}
    # The path to current city
    parents = {}

    while priorityQueue:
        # get the city with minimum fCost from priority queue
        currentFCost, current = heapq.heappop(priorityQueue)
        # if goal city reached, construct the path using parents dictionary
        if current == goalCity:
            path = [current]
            while current in parents:
                current = parents[current]
                path.append(current)
            path.reverse()
            return path
        
        # add current city visited list
        visitedList.add(current)
        for neighbor, cost in map[current].items():
            # if neighbor already in visited list, skip it
            if neighbor in visitedList:
                continue

            currentGCost = gCost[current] + cost
            # Calculate gCost and fCost for neighbor city and add it to priority queue
            if neighbor not in gCost or currentGCost < gCost[neighbor]:
                parents[neighbor] = current
                gCost[neighbor] = currentGCost
                # fCost = gCost + heuristic cost
                fCost[neighbor] = currentGCost + heuristic(neighbor, goalCity)
                heapq.heappush(priorityQueue, (fCost[neighbor], neighbor))
    return None

startSearch = input("Enter start city name: ")
startSearch = ' '.join(word.capitalize() for word in startSearch.split())

goalSearch = input("Enter goal city name: ")
goalSearch = ' '.join(word.capitalize() for word in goalSearch.split())

path = aStarSearch(map, startSearch, goalSearch)
print(path)