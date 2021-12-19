import random
import pylab
import numpy as np

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

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

class ResistantVirus(SimpleVirus):
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        super().__init__(maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb
    def getResistances(self):
        return self.resistances
    def getMutProb(self):
        return self.mutProb
    def isResistantTo(self, drug):
        return self.resistances.get(drug, False)
    def reproduce(self, popDensity, activeDrugs):
        for d in activeDrugs:
            if not self.resistances.get(d, False):
                raise NoChildException
        if random.random() < self.maxBirthProb * (1 - popDensity):
            sr = {d: r ^ (random.random() < self.mutProb) for 
                  d, r in self.resistances.items()}
            return ResistantVirus(self.maxBirthProb, self.clearProb, sr, self.mutProb)
        raise NoChildException

virus = ResistantVirus(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)
virus.reproduce(0, []) 