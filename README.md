# MITx-6.00.2x-Introduction-to-Computational-Thinking-and-Data-Science

6.00.2x apply how to use computation to accomplish a variety of goals and provides you with a brief introduction to a variety of topics in computational problem solving . This course is aimed at students with some prior programming experience in Python and a rudimentary knowledge of computational complexity. You will spend a considerable amount of time writing programs to implement the concepts covered in the course. For example, you will write a program that will simulate a robot vacuum cleaning a room or will model the population dynamics of viruses replicating and drug treatments in a patient's body.

# Enviromment

* Windows 10
* VSCode
* Python 3

# Topics

# Topics covered include:

* Advanced programming in Python 3
* Knapsack problem, Graphs and graph optimization
* Dynamic programming
* Plotting with the pylab package
* Random walks
* Probability, Distributions
* Monte Carlo simulations
* Curve fitting
* Statistical fallacies

# Project 01

## Space Cows Introduction
A colony of Aucks (super-intelligent alien bioengineers) has landed on Earth and has created new species of farm animals! The Aucks are performing their experiments on Earth, and plan on transporting the mutant animals back to their home planet of Aurock. In this problem set, you will implement algorithms to figure out how the aliens should shuttle their experimental animals back across space.

## Transporting Cows Across Space!

The aliens have succeeded in breeding cows that jump over the moon! Now they want to take home their mutant cows. The aliens want to take all chosen cows back, but their spaceship has a weight limit and they want to minimize the number of trips they have to take across the universe. Somehow, the aliens have developed breeding technology to make cows with only integer weights.

The data for the cows to be transported is stored in ps1_cow_data.txt. All of your code for Part A should go into ps1.py.

First we need to load the cow data from the data file ps1_cow_data.txt, this has already been done for you and should let you begin working on the rest of this problem. If you are having issues getting the ps1_cow_data.txt to load, be sure that you have it in the same folder as the ps1.py that you are running.

You can expect the data to be formatted in pairs of x,y on each line, where x is the name of the cow and y is a number indicating how much the cow weighs in tons, and that all of the cows have unique names. Here are the first few lines of ps1_cow_data.txt:

Maggie,3
Herman,7
Betsy,9
...

## Part 1: Greedy Cow Transport

One way of transporting cows is to always pick the **heaviest cow that will fit** onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

## Assumptions:

The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
All the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.

## Example:

Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].

For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].

## Part 2: : Brute Force Cow Transport

Another way to transport the cows is to look at every possible combination of trips and pick the best one. This is an example of a brute force algorithm.

Implement a brute force algorithm to find the minimum number of trips needed to take all the cows across the universe in the function brute_force_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

## Notes:

Make sure not to mutate the dictionary of cows!
In order to enumerate all possible combinations of trips, you will want to work with set partitions. We have provided you with a helper function called get_partitions that generates all the set partitions for a set of cows. More details on this function are provided below.

## Assumptions:

* Assume that order doesn't matter. (1) [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips. (2) [[1,2],[3,4]] and [[2,1],[3,4]] are considered the same partitions of [1,2,3,4].
* You can assume that all the cows are between 0 and 100 tons in weight.
* All the cows have unique names.
* If multiple cows weigh the same amount, break ties arbitrarily.
* The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.

Helper function **get_partitions** in **ps1_partitions.py**:

To generate all the possibilities for the brute force method, you will want to work with set partitions.

For instance, all the possible 2-partitions of the list [1,2,3,4] are [[1,2],[3,4]], [[1,3],[2,4]], [[2,3],[1,4]], [[1],[2,3,4]], [[2],[1,3,4]], [[3],[1,2,4]], [[4],[1,2,3]].

To help you with creating partitions, we have included a helper function get_partitions(L) that takes as input a list and returns a generator that contains all the possible partitions of this list, from 0-partitions to n-partitions, where n is the length of this list.

You can review more on generators in the Lecture 2 Exercise 1. To use generators, you must iterate over the generator to retrieve the elements; you cannot index into a generator! For instance, the recommended way to call get_partitions on a list [1,2,3] is the following. Try it out in ps1_partitions.py to see what is printed!

for partition in get_partitions([1,2,3]):
    print(partition)

## Example:

Suppose the spaceship has a cargo weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The brute force algorithm will first try to fit them on only one trip, ["Jesse", "Maybel", "Callie", "Maggie"]. Since this trip contains 16 tons of cows, it is over the weight limit and does not work. Then the algorithm will try fitting them on all combinations of two trips. Suppose it first tries [["Jesse", "Maggie"], ["Maybel", "Callie"]]. This solution will be rejected because Jesse and Maggie together are over the weight limit and cannot be on the same trip. The algorithm will continue trying two trip partitions until it finds one that works, such as [["Jesse", "Callie"], ["Maybel", "Maggie"]].

The final result is then [["Jesse", "Callie"], ["Maybel", "Maggie"]]. Note that depending on which cow it tries first, the algorithm may find a different, optimal solution. Another optimal result could be [["Jesse", "Maybel"],["Callie", "Maggie"]].

# Project 2

## Simulation Overview

iRobot is a company (started by MIT alumni and faculty) that sells the Roomba vacuuming robot (watch one of the product videos to see these robots in action). Roomba robots move around the floor, cleaning the area they pass over.

In this problem set, you will code a simulation to compare how much time a group of Roomba-like robots will take to clean the floor of a room using two different strategies.

The following simplified model of a single robot moving in a square 5x5 room should give you some intuition about the system we are simulating.

The robot starts out at some random position in the room, and with a random direction of motion. The illustrations below show the robot's position (indicated by a black dot) as well as its direction (indicated by the direction of the red arrowhead).

![alt text](https://github.com/ricardpaschoeto/MITx-6.00.2x-Introduction-to-Computational-Thinking-and-Data-Science/blob/master/PS02/pset2/iRobot.png?raw=true)

## Simulation Details
Here are additional details about the simulation model. Read these carefully.

* Multiple robots
In general, there are N > 0 robots in the room, where N is given. For simplicity, assume that robots are points and can pass through each other or occupy the same point without interfering.

* The room
The room is rectangular with some integer width w and height h, which are given. Initially the entire floor is dirty. A robot cannot pass through the walls of the room. A robot may not move to a point outside the room.

* Tiles
You will need to keep track of which parts of the floor have been cleaned by the robot(s). We will divide the area of the room into 1x1 tiles (there will be w * h such tiles). When a robot's location is anywhere in a tile, we will consider the entire tile to be cleaned (as in the pictures above). By convention, we will refer to the tiles using ordered pairs of integers: (0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), ..., (w-1, h-1).

* Robot motion rules
Each robot has a position inside the room. We'll represent the position using coordinates (x, y) which are floats satisfying 0 ≤ x < w and 0 ≤ y < h. In our program we'll use instances of the Position class to store these coordinates.

    * A robot has a direction of motion. We'll represent the direction using an integer d satisfying 0 ≤ d < 360, which gives an angle in degrees.

    * All robots move at the same speed s, a float, which is given and is constant throughout the simulation. Every time-step, a robot moves in its direction of motion by s units.

    * If a robot detects that it will hit the wall within the time-step, that time step is instead spent picking a new direction at random. The robot will attempt to move in that direction on the next time step, until it reaches another wall.

* Termination
The simulation ends when a specified fraction of the tiles in the room have been cleaned.
