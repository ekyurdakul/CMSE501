from agent import *
import numpy as np

class Simulation:
    def __init__(self,nofagents,time,nofpredictors,crowded,updateEvery):
        self.__agents = []
        self.__attendances = []
        self.__time = time
        self.__updateTime = updateEvery
        #Replicate predictors randomly
        preds = []
        for i in range(nofpredictors*nofagents):
            ri = rnd.randint(0,len(predictors)-1)
            preds.append(predictors[ri])
        #Create agents
        for i in range(nofagents):
            newagent = Agent(crowded)
            #Randomly pick predictors
            for j in range(nofpredictors):
                ri = rnd.randint(0,len(preds)-1)
                newagent.addPredictor(preds[ri])
                del preds[ri]
            self.__agents.append(newagent)
            
    def simulate(self):
        #Simulate for time amount of weeks
        for i in range(self.__time):
            newAtt = 0
            #Determine the new attendance
            for a in self.__agents:
                newAtt += a.isGoing(self.__attendances)
            #If it is time to update active predictors
            if i % self.__updateTime == 0:
                #Update agent predictors according to the new attendance
                for a in self.__agents:
                    a.updatePredictors(self.__attendances,newAtt)
            #Record the new attendance
            self.__attendances.append(newAtt)
        return self.__attendances