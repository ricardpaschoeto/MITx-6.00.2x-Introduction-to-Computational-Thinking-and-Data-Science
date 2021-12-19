import random
import pylab

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

class SimpleVirus(object):
    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
    def getMaxBirthProb(self):
        return self.maxBirthProb
    def getClearProb(self):
        return self.clearProb
    def doesClear(self):
        return random.random() < self.clearProb
    def reproduce(self, popDensity):
        if random.random() < self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

class Patient(object):
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
    def getViruses(self):
        return self.viruses
    def getMaxPop(self):
        return self.maxPop
    def getTotalPop(self):
        return len(self.viruses)
    def update(self):
        self.viruses = [v for v in self.viruses if not v.doesClear()]
        dens = self.getTotalPop() / self.getMaxPop()
        for v in self.viruses:
            try:
                self.viruses.append(v.reproduce(dens))
            except NoChildException:
                pass
        return self.getTotalPop()

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials):
    steps = 300
    pop = [0] * steps
    for _ in range(numTrials):
        v = [SimpleVirus(maxBirthProb, clearProb) for _ in range(numViruses)]
        p = Patient(v, maxPop)
        pop = [e + p.update() for e in pop]
    y = [e / numTrials for e in pop]
    pylab.plot(y, label = "SimpleVirus")
    print(y)   
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

simulationWithoutDrug(1, 10, 1.0, 0.0, 1)