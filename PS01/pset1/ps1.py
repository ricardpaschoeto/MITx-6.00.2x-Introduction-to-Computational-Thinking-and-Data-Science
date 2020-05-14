###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()
    
    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    listTrips = []
    sorted_cows = sorted(cows.items(), key=lambda k: k[1], reverse = True)
    while(len(sorted_cows) > 0):
        new_limit = limit
        if(sorted_cows[-1][1] < new_limit):
            trip = []
            ii = 0
            while(ii < len(sorted_cows)):
                cow = sorted_cows[ii]
                if(cow[1] <= new_limit):
                    trip_cow = sorted_cows.pop(ii)
                    new_limit = new_limit - trip_cow[1]
                    trip.append(trip_cow[0])
                    ii = 0;
                else:
                    ii = ii + 1
            listTrips.append(trip)
        else:
            break
               
    return listTrips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    listTrips = []
    result = []
    for partition in get_partitions(cows.items()):
        for cws in partition:
            s = 0
            for cow in cws:
                 s = s + cow[1]

            if(s <= limit):
                if(listTrips.count(cws) == 0):
                    listTrips.append(cws)
            
    count = 0
    for trip in listTrips:
        if(len(trip) == 1):
            count = count + 1
    if(count == len(listTrips)):
        for trip in listTrips:
            for cow in trip:
                result.append([cow[0]])
        return result;
    
    higher = 0
    for trip in listTrips:
        s = 0
        for cow in trip:
            s = s + cow[1]
        if(s > higher):
            higher = s
            
    for trip in listTrips:
        s = 0
        for cow in trip:
            s = s + cow[1]
        if (s == higher):
            result.append([c[0] for c in trip])
             
    return result

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(load_cows("ps1_cow_data.txt"), 10)
    end = time.time()
    print(end - start)
    
    start = time.time()
    brute_force_cow_transport(load_cows("ps1_cow_data.txt"), 10)
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# print(greedy_cow_transport({'Patches': 12, 'Daisy': 50, 'Lilly': 24, 'Willow': 35, 'Betsy': 65, 'Coco': 10, 'Rose': 50, 'Dottie': 85, 'Buttercup': 72, 'Abby': 38}, 100))
# print('\n')
# print(greedy_cow_transport({'Lotus': 10, 'Patches': 60, 'Clover': 5, 'Polaris': 20, 'Muscles': 65, 'Milkshake': 75, 'Miss Bella': 15, 'MooMoo': 85, 'Horns': 50, 'Louis': 45}, 100))

#print(brute_force_cow_transport(load_cows("ps1_cow_data.txt"), 10))
#print(brute_force_cow_transport({'Horns': 25, 'MooMoo': 50, 'Boo': 20, 'Lotus': 40, 'Milkshake': 40, 'Miss Bella': 25}, 100))
#print(brute_force_cow_transport({'Betsy': 65, 'Buttercup': 72, 'Daisy': 50}, 75))
#print(brute_force_cow_transport({'Betsy': 39, 'Starlight': 54, 'Buttercup': 11, 'Luna': 41}, 145))

compare_cow_transport_algorithms()

