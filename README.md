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


