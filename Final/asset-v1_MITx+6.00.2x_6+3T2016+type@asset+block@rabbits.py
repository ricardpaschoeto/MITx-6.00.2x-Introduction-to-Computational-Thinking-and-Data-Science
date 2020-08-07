import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    prepo = 1.0 -(CURRENTRABBITPOP/MAXRABBITPOP)
    if(prepo >= random.random()):
        CURRENTRABBITPOP += 1 
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    if (CURRENTRABBITPOP > 10):
        pfoxhunt = CURRENTRABBITPOP/MAXRABBITPOP
        if (pfoxhunt >= random.random()):
            if(random.random() <= 1/3):
                CURRENTFOXPOP += 1
                CURRENTRABBITPOP -= 1
        else:
            if(random.random() <= 1/10):
                if(CURRENTFOXPOP > 10):
                    CURRENTFOXPOP -= 1
                else:
                    CURRENTFOXPOP += 1
    else:
        CURRENTRABBITPOP += 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        if (len(rabbit_populations) < MAXRABBITPOP):
            rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    return (rabbit_populations,fox_populations)

res = runSimulation(200)

coeff = pylab.polyfit(range(len(res[1])), res[1], 2)

pylab.plot(pylab.polyval(coeff, range(len(res[1]))))

# res = runSimulation(200)
# #print(res[1])
# pylab.plot(range(200),res[1])

        
        
        
        
